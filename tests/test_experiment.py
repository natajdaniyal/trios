import os
import sys


# اضافه کردن مسیر اصلی پروژه
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from explorer import Profile
from experiment import run_test



print("\n🧪 TRIOS EXPERIMENT TEST")
print("=" * 35)


username = "__experiment_test__"
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




# ساخت کاربر آزمایشی

profile = Profile(username)


if profile.exists():
    profile.delete_account()



profile.create(password)



# اجرای آزمایش فعلی پروژه
# چون نسخه فعلی آزمایش ورودی می‌گیرد،
# فعلاً فقط بررسی می‌کنیم که تابع وجود دارد.

check(
    callable(run_test),
    "Experiment Function Exists"
)



# بررسی اتصال آزمایش به پروفایل

profile.add_experiment(
    "Test Experiment",
    "Prediction",
    "Result",
    True
)



data = profile.load()



check(
    len(data["experiments"]) == 1,
    "Experiment Stored In Profile"
)



check(
    data["experiments"][0]["name"] == "Test Experiment",
    "Experiment Name Saved"
)



check(
    data["experiments"][0]["correct"] is True,
    "Experiment Result Saved"
)



# پاکسازی

profile.delete_account()



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")



if failed == 0:

    print("\n🟢 Experiment System Healthy")

else:

    print("\n🔴 Experiment System Has Problems")