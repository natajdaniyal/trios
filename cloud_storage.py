import json
from pathlib import Path

import streamlit as st


_TABLE_READY = False
_MIGRATION_DONE = False


def cloud_enabled():
    try:
        secrets = st.secrets.to_dict()
        config = secrets.get("connections", {}).get("trios_db", {})
        return bool(config.get("url"))
    except Exception:
        return False


def _database_url():
    secrets = st.secrets.to_dict()
    url = secrets["connections"]["trios_db"]["url"]
    return url.replace("postgresql+psycopg://", "postgresql://", 1)


def _connection():
    import psycopg

    return psycopg.connect(_database_url())


def _ensure_table():
    global _TABLE_READY
    if _TABLE_READY:
        return

    with _connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS trios_profiles (
                username VARCHAR(255) PRIMARY KEY,
                profile_json TEXT NOT NULL
            )
            """
        )
        conn.commit()
    _TABLE_READY = True


def _decode(row):
    if row is None:
        return None
    value = row[0] if not isinstance(row, dict) else row.get("profile_json")
    return json.loads(value)


def get_profile(username):
    _ensure_table()
    with _connection() as conn:
        row = conn.execute(
            "SELECT profile_json FROM trios_profiles WHERE username = %s",
            (username,),
        ).fetchone()
    return _decode(row)


def list_profiles():
    _ensure_table()
    with _connection() as conn:
        rows = conn.execute("SELECT profile_json FROM trios_profiles").fetchall()
    return [json.loads(row[0]) for row in rows]


def save_profile(data):
    _ensure_table()
    username = data["username"]
    payload = json.dumps(data, ensure_ascii=False)

    with _connection() as conn:
        updated = conn.execute(
            """
            UPDATE trios_profiles
            SET profile_json = %s
            WHERE username = %s
            """,
            (payload, username),
        )
        if updated.rowcount == 0:
            conn.execute(
                """
                INSERT INTO trios_profiles (username, profile_json)
                VALUES (%s, %s)
                """,
                (username, payload),
            )
        conn.commit()


def delete_profile(username):
    _ensure_table()
    with _connection() as conn:
        result = conn.execute(
            "DELETE FROM trios_profiles WHERE username = %s",
            (username,),
        )
        conn.commit()
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
