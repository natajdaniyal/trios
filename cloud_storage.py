import hashlib
import json
import secrets
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
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS trios_sessions (
                token_hash VARCHAR(64) PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                last_activity_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
            """
        )
        conn.execute(
            """
            ALTER TABLE trios_sessions
            ADD COLUMN IF NOT EXISTS last_activity_at TIMESTAMPTZ
            """
        )
        conn.execute(
            """
            UPDATE trios_sessions
            SET last_activity_at = created_at
            WHERE last_activity_at IS NULL
            """
        )
        conn.execute(
            """
            ALTER TABLE trios_sessions
            ALTER COLUMN last_activity_at SET DEFAULT NOW()
            """
        )
        conn.execute(
            """
            ALTER TABLE trios_sessions
            ALTER COLUMN last_activity_at SET NOT NULL
            """
        )
        conn.commit()
    _TABLE_READY = True


def _hash_session_token(token):
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_session(username):
    _ensure_table()
    token = secrets.token_urlsafe(32)
    token_hash = _hash_session_token(token)

    with _connection() as conn:
        conn.execute(
            """
            INSERT INTO trios_sessions (token_hash, username, last_activity_at)
            VALUES (%s, %s, NOW())
            """,
            (token_hash, username),
        )
        conn.commit()
    return token


def get_session_user(token):
    if not token:
        return None

    _ensure_table()
    token_hash = _hash_session_token(token)

    with _connection() as conn:
        row = conn.execute(
            "SELECT username FROM trios_sessions WHERE token_hash = %s",
            (token_hash,),
        ).fetchone()
        if row:
            conn.execute(
                "UPDATE trios_sessions SET last_activity_at = NOW() WHERE token_hash = %s",
                (token_hash,),
            )
            conn.commit()

    return row[0] if row else None


def touch_session(token):
    """Refresh the activity timestamp for a valid web session."""
    if not token:
        return False

    _ensure_table()
    token_hash = _hash_session_token(token)

    with _connection() as conn:
        result = conn.execute(
            """
            UPDATE trios_sessions
            SET last_activity_at = NOW()
            WHERE token_hash = %s
            """,
            (token_hash,),
        )
        conn.commit()

    return result.rowcount > 0


def get_account_stats():
    """Return aggregate account statistics based on currently valid sessions."""
    _ensure_table()

    with _connection() as conn:
        row = conn.execute(
            """
            SELECT
                (SELECT COUNT(*) FROM trios_profiles) AS total_accounts,
                (
                    SELECT COUNT(DISTINCT username)
                    FROM trios_sessions
                ) AS active_users,
                (
                    SELECT COUNT(*)
                    FROM trios_sessions
                ) AS active_sessions
            """
        ).fetchone()

    return {
        "total_accounts": row[0],
        "active_users": row[1],
        "active_sessions": row[2],
    }


def delete_session(token):
    if not token:
        return False

    _ensure_table()
    token_hash = _hash_session_token(token)

    with _connection() as conn:
        result = conn.execute(
            "DELETE FROM trios_sessions WHERE token_hash = %s",
            (token_hash,),
        )
        conn.commit()
    return result.rowcount > 0


def delete_sessions_for_user(username):
    _ensure_table()

    with _connection() as conn:
        result = conn.execute(
            "DELETE FROM trios_sessions WHERE username = %s",
            (username,),
        )
        conn.commit()
    return result.rowcount


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
        conn.execute(
            "DELETE FROM trios_sessions WHERE username = %s",
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
