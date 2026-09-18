import json
from pathlib import Path

import streamlit as st


_TABLE_READY = False
_MIGRATION_DONE = False


def cloud_enabled():
    try:
        connections = st.secrets.get("connections", {})
        config = connections.get("trios_db", {})
        return bool(config.get("url"))
    except Exception:
        return False


def _connection():
    return st.connection("trios_db", type="sql")


def _ensure_table():
    global _TABLE_READY
    if _TABLE_READY:
        return

    conn = _connection()
    with conn.session as session:
        session.execute(
            """
            CREATE TABLE IF NOT EXISTS trios_profiles (
                username VARCHAR(255) PRIMARY KEY,
                profile_json TEXT NOT NULL
            )
            """
        )
        session.commit()
    _TABLE_READY = True


def _decode(row):
    if row is None:
        return None
    value = row[0] if not isinstance(row, dict) else row.get("profile_json")
    return json.loads(value)


def get_profile(username):
    _ensure_table()
    with _connection().session as session:
        row = session.execute(
            "SELECT profile_json FROM trios_profiles WHERE username = :username",
            {"username": username},
        ).fetchone()
    return _decode(row)


def list_profiles():
    _ensure_table()
    with _connection().session as session:
        rows = session.execute("SELECT profile_json FROM trios_profiles").fetchall()
    return [json.loads(row[0]) for row in rows]


def save_profile(data):
    _ensure_table()
    username = data["username"]
    payload = json.dumps(data, ensure_ascii=False)

    with _connection().session as session:
        updated = session.execute(
            """
            UPDATE trios_profiles
            SET profile_json = :profile_json
            WHERE username = :username
            """,
            {"username": username, "profile_json": payload},
        )
        if updated.rowcount == 0:
            session.execute(
                """
                INSERT INTO trios_profiles (username, profile_json)
                VALUES (:username, :profile_json)
                """,
                {"username": username, "profile_json": payload},
            )
        session.commit()


def delete_profile(username):
    _ensure_table()
    with _connection().session as session:
        result = session.execute(
            "DELETE FROM trios_profiles WHERE username = :username",
            {"username": username},
        )
        session.commit()
    return result.rowcount > 0


def migrate_local_profiles():
    """Copy legacy local JSON profiles into the cloud database once available."""
    global _MIGRATION_DONE
    if _MIGRATION_DONE or not cloud_enabled():
        return 0

    _MIGRATION_DONE = True
    data_dir = Path("data")
    if not data_dir.is_dir():
        return 0

    migrated = 0
    for path in data_dir.glob("*.json"):
        if path.name == "session.json":
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            username = data.get("username")
            if not username or get_profile(username) is not None:
                continue
            save_profile(data)
            migrated += 1
        except (OSError, json.JSONDecodeError):
            continue

    return migrated
