import os
import sys


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from command import CommandCenter
from state import state



print("\n🎮 TRIOS COMMAND SYSTEM TEST")
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




# ساخت مرکز فرمان

command_center = CommandCenter()



check(
    command_center is not None,
    "Command Center Exists"
)



check(
    hasattr(command_center, "execute"),
    "Execute Function Exists"
)



# ذخیره وضعیت اولیه

old_x = state.x



# اجرای فرمان حرکت راست

command_center.execute("RIGHT")



check(
    state.x == old_x + 1,
    "RIGHT Command Updates State"
)



# اجرای فرمان حرکت چپ

command_center.execute("LEFT")



check(
    state.x == old_x,
    "LEFT Command Updates State"
)



# تست ریست

state.x = 50


command_center.execute("RESET")



check(
    state.x == 0,
    "RESET Command Works"
)



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")



if failed == 0:

    print("\n🟢 Command System Healthy")

else:

    print("\n🔴 Command System Has Problems")