import os
import sys


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from events import events



print("\n📨 TRIOS EVENT SYSTEM TEST")
print("=" * 35)


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




# وجود سیستم رویداد

check(
    events is not None,
    "Event System Exists"
)



# بررسی اینکه EventBus متدهای لازم را دارد

check(
    hasattr(events, "emit"),
    "Emit Function Exists"
)



check(
    hasattr(events, "subscribe"),
    "Subscribe Function Exists"
)



check(
    hasattr(events, "__dict__"),
    "EventBus Structure Exists"
)



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")



if failed == 0:

    print("\n🟢 Event System Healthy")

else:

    print("\n🔴 Event System Needs Review")