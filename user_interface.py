"""User-facing actions shared by console and web interfaces.

This module contains no UI framework code. It provides small operations that
an interface can call, so a web interface does not need to reproduce the
console menu or depend on numeric menu choices.
"""

from tools.explorer import Profile


def user_profile(username):
    """Return the stored profile data for an existing user."""
    profile = Profile(username)
    if not profile.exists():
        raise ValueError("User account does not exist.")
    return profile.load()


def authenticate_user(username, password):
    """Authenticate an existing user, start its session, and return profile data."""
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

    profile.create_session()
    return profile.load()


def recover_user(username, password):
    """Recover an existing account and start its session."""
    return authenticate_user(username, password)


def create_user(username, password):
    """Create a new user account, start its session, and return profile data."""
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    if password is None or password == "":
        raise ValueError("Password cannot be empty.")

    profile = Profile(username)
    if not profile.create(password):
        raise ValueError("User account already exists.")

    profile.create_session()
    return profile.load()


def restore_user_session():
    """Return the stored session's profile data, or None when no session exists."""
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
    """Clear the local session for a user without deleting the account."""
    profile = Profile(username)
    return profile.clear_session()


def delete_user(username):
    """Delete an existing user account."""
    profile = Profile(username)
    return profile.delete_account()
