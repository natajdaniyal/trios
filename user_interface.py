"""User-facing actions shared by console and web interfaces.

This module contains no UI framework code. It provides small operations that
an interface can call, so a web interface does not need to reproduce the
console menu or depend on numeric menu choices.
"""

import json
import os


def _local_profile(username):
    """Load the legacy local Profile only when cloud storage is unavailable."""
    from tools.explorer import Profile
    return _local_profile(username)


def _cloud_enabled():
    from cloud_storage import cloud_enabled
    return cloud_enabled()

def _cloud_migrate():
    from cloud_storage import migrate_local_profiles
    migrate_local_profiles()

def _cloud():
    if _cloud_enabled():
        _cloud_migrate()
        return True
    return False


def user_profile(username):
    """Return the stored profile data for an existing user."""
    if _cloud():
        from cloud_storage import get_profile
        data = get_profile(username)
        if data is None:
            raise ValueError("User account does not exist.")
        return data

    profile = _local_profile(username)
    if not profile.exists():
        raise ValueError("User account does not exist.")
    return profile.load()


def authenticate_user(username, password):
    """Authenticate an existing TRIOS account."""
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    if password is None or password == "":
        raise ValueError("Password cannot be empty.")

    if _cloud():
        data = user_profile(username)
        if data.get("auth_method", "trios") != "trios" or data.get("password") != password:
            raise ValueError("Incorrect password.")
        return data

    profile = _local_profile(username)
    if not profile.exists():
        raise ValueError("User account does not exist.")
    if not profile.check_password(password):
        raise ValueError("Incorrect password.")

    return profile.load()


def recover_user(username, password):
    """Recover an existing TRIOS account using its own credentials."""
    return authenticate_user(username, password)


def create_user(username, password):
    """Create a new user account with the native TRIOS authentication system."""
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    if password is None or password == "":
        raise ValueError("Password cannot be empty.")

    if _cloud():
        from cloud_storage import get_profile, save_profile
        if get_profile(username) is not None:
            raise ValueError("User account already exists.")
        data = {"username": username, "password": password, "auth_method": "trios", "level": 1, "experiments": [], "total_attempts": 0, "correct_answers": 0, "accuracy": 0}
        save_profile(data)
        return data

    profile = _local_profile(username)
    if not profile.create(password):
        raise ValueError("User account already exists.")

    return profile.load()


def _iter_profiles():
    """Yield existing local TRIOS profiles."""
    if _cloud():
        from cloud_storage import list_profiles
        yield from list_profiles()
        return

    if not os.path.isdir("data"):
        return

    for filename in os.listdir("data"):
        if not filename.endswith(".json") or filename == "session.json":
            continue

        username = filename[:-5]
        profile = _local_profile(username)
        if profile.exists():
            try:
                yield profile.load()
            except (OSError, json.JSONDecodeError):
                continue


def google_profile(google_sub):
    """Return the TRIOS profile linked to a Google identity, if any."""
    if not google_sub:
        return None

    for data in _iter_profiles():
        if (
            data.get("auth_method") == "google"
            and data.get("google_sub") == google_sub
        ):
            return data

    return None


def google_email_profile(email):
    """Return any TRIOS profile already using the supplied email."""
    if not email:
        return None

    email = email.strip().lower()
    for data in _iter_profiles():
        if data.get("google_email", "").strip().lower() == email:
            return data

        # A native TRIOS account may not have a stored email yet. This branch
        # intentionally does not match it: email is not the TRIOS identity key.

    return None


def create_google_user(username, google_sub, google_email=None, google_name=None):
    """Create one TRIOS profile for a Google identity, rejecting duplicates."""
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    if not google_sub:
        raise ValueError("Google identity is missing.")

    if google_profile(google_sub) is not None:
        raise ValueError("This Google account already has a TRIOS account.")

    if google_email_profile(google_email) is not None:
        raise ValueError("This Google account is already linked to a TRIOS account.")

    if _cloud():
        from cloud_storage import get_profile, save_profile
        if get_profile(username) is not None:
            raise ValueError("User account already exists.")
        data = {"username": username, "password": None, "auth_method": "google", "google_sub": google_sub, "google_email": google_email or "", "google_name": google_name or "", "level": 1, "experiments": [], "total_attempts": 0, "correct_answers": 0, "accuracy": 0}
        save_profile(data)
        return data

    profile = _local_profile(username)
    if not profile.create_google(google_sub, google_email, google_name):
        raise ValueError("User account already exists.")

    return profile.load()


def restore_user_session():
    """Legacy console-session helper; web UI uses Streamlit session state."""
    username = _local_profile("").get_session()
    if not username:
        return None

    profile = _local_profile(username)
    if not profile.exists():
        profile.clear_session()
        return None

    return profile.load()


def user_report(username):
    """Return the stored report data for an existing user."""
    return user_profile(username)


def logout_user(username):
    """Clear the legacy local session for a user."""
    profile = _local_profile(username)
    return profile.clear_session()


def delete_user(username):
    """Delete an existing user account."""
    if _cloud():
        from cloud_storage import delete_profile
        return delete_profile(username)

    profile = _local_profile(username)
    return profile.delete_account()
