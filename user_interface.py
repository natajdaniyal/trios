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


def user_report(username):
    """Return the stored report data for an existing user."""
    return user_profile(username)


def logout_user(username):
    """Clear the local console session for a user."""
    profile = Profile(username)
    return profile.clear_session()


def delete_user(username):
    """Delete an existing user account."""
    profile = Profile(username)
    return profile.delete_account()
