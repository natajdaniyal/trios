import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from explorer import Profile

print("\nTRIOS PROFILE & SESSION TEST")
print("=" * 40)

username = "__test_user__"
password = "1234"

passed = 0
failed = 0


def check(condition, message):
    global passed, failed

    if condition:
        print(f"PASS: {message}")
        passed += 1
    else:
        print(f"FAIL: {message}")
        failed += 1


profile = Profile(username)

if profile.exists():
    profile.delete_account()

profile.clear_session()

check(profile.create(password), "Create Account")
check(profile.exists(), "Profile File Created")
check(profile.check_password(password), "Correct Password")
check(not profile.check_password("9999"), "Wrong Password")
check(not profile.create(password), "Duplicate Username Blocked")

profile.create_session()

check(profile.get_session() == username, "Session Created")

new_profile = Profile(username)

check(
    new_profile.get_session() == username,
    "Session Persists"
)

profile.clear_session()

check(
    profile.get_session() is None,
    "Session Cleared"
)

check(
    profile.exists(),
    "Account Preserved After Device Logout"
)

profile.create_session()

check(
    profile.get_session() == username,
    "Session Recreated"
)

check(
    profile.delete_account(),
    "Delete Account"
)

check(
    not profile.exists(),
    "Profile File Removed"
)

check(
    profile.get_session() is None,
    "Session Removed With Account"
)

print("\n" + "=" * 40)
print(f"Passed : {passed}")
print(f"Failed : {failed}")

if failed == 0:
    print("\nPROFILE & SESSION SYSTEM HEALTHY")
else:
    print("\nPROFILE & SESSION SYSTEM HAS PROBLEMS")
