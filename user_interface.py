"""User-facing actions shared by console and web interfaces.

This module contains no UI framework code. It provides small operations that
an interface can call, so a web interface does not need to reproduce the
console menu or depend on numeric menu choices.
"""

import json
import os

from tools.explorer import Profile


def user_profile(username):
    """Return the stored profile data for an existing user."""
    profile = Profile(username)
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

    profile = Profile(username)
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

    profile = Profile(username)
    if not profile.create(password):
        raise ValueError("User account already exists.")

    return profile.load()


def _iter_profiles():
    """Yield existing local TRIOS profiles."""
    if not os.path.isdir("data"):
        return

    for filename in os.listdir("data"):
        if not filename.endswith(".json") or filename == "session.json":
            continue

        username = filename[:-5]
        profile = Profile(username)
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


def create_google_user(username, google_sub, google_email=None, google_name=None):
    """Create one TRIOS profile for a Google identity, rejecting duplicates."""
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    if not google_sub:
        raise ValueError("Google identity is missing.")

    if google_profile(google_sub) is not None:
        raise ValueError("This Google account already has a TRIOS account.")

    profile = Profile(username)
    if not profile.create_google(google_sub, google_email, google_name):
        raise ValueError("User account already exists.")

    return profile.load()


def restore_user_session():
    """Legacy console-session helper; web UI should use Streamlit session state."""
    username = Profile("").get_session()
    if not username:
        return None

    profile = Profile(username)
    if not profile.exists():
        profile.clear_session()
        return None

    return profile.load()


def user_report(username):
    """Return the stored report data for an existing user."""
    return user_profile(username)


def logout_user(username):
    """Clear the legacy local session for a user."""
    profile = Profile(username)
    return profile.clear_session()


def delete_user(username):
    """Delete an existing user account."""
    profile = Profile(username)
    return profile.delete_account()
