import os
import sys

# اضافه کردن مسیر پروژه اصلی
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from explorer import Profile


print("\n🧪 TRIOS PROFILE TEST")
print("=" * 35)


username = "__test_user__"
password = "1234"


passed = 0
failed = 0


def check(condition, message):

    global passed, failed

    if condition:
        print(f"✅ {message}")
        passed += 1

    else:
        print(f"❌ {message}")
        failed += 1



# ساخت پروفایل تستی
profile = Profile(username)


# اگر از قبل وجود داشت پاک شود
if profile.exists():
    profile.delete_account()



# تست ساخت حساب

created = profile.create(password)

check(
    created,
    "Create Account"
)



# تست ساخته شدن فایل

check(
    profile.exists(),
    "Profile File Created"
)



# تست رمز درست

check(
    profile.check_password(password),
    "Correct Password"
)



# تست رمز غلط

check(
    not profile.check_password("9999"),
    "Wrong Password"
)



# تست جلوگیری از حساب تکراری

duplicate = profile.create(password)

check(
    not duplicate,
    "Duplicate Username Blocked"
)



# تست حذف حساب

deleted = profile.delete_account()

check(
    deleted,
    "Delete Account"
)



# تست حذف کامل فایل

check(
    not profile.exists(),
    "Profile File Removed"
)



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:

    print("\n🟢 Profile System Healthy")

else:

    print("\n🔴 Profile System Has Problems")