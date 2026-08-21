import os
import sys


# اضافه کردن مسیر اصلی پروژه
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from explorer import Profile
from report import Report



print("\n📊 TRIOS REPORT TEST")
print("=" * 35)


username = "__report_test__"
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




# ساخت کاربر تستی

profile = Profile(username)


if profile.exists():
    profile.delete_account()



profile.create(password)



# -----------------------------
# Test 1
# بررسی وجود اطلاعات
# -----------------------------

data = profile.load()


check(
    data["username"] == username,
    "Username Loaded"
)



# -----------------------------
# Test 2
# ثبت آزمایش آزمایشی
# -----------------------------

profile.add_experiment(
    "Gravity Test",
    "Bodies attract each other",
    "Successful",
    True
)


data = profile.load()


check(
    len(data["experiments"]) == 1,
    "Experiment Saved"
)



# -----------------------------
# Test 3
# بررسی تعداد تلاش
# -----------------------------

check(
    data["total_attempts"] == 1,
    "Attempt Counter"
)



# -----------------------------
# Test 4
# بررسی دقت
# -----------------------------

check(
    data["accuracy"] == 100,
    "Accuracy Calculation"
)



# -----------------------------
# Test 5
# ساخت گزارش
# -----------------------------

report = Report()

result = profile.get_report()



check(
    result["attempts"] == 1,
    "Report Data Generated"
)



# پاکسازی

profile.delete_account()



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")



if failed == 0:

    print("\n🟢 Report System Healthy")

else:

    print("\n🔴 Report System Has Problems")