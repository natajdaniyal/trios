import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from command import CommandCenter
from state import state



print("\n🌌 TRIOS FULL SYSTEM INTEGRATION TEST")
print("=" * 40)


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



command = CommandCenter()



check(
    command is not None,
    "Command System Connected"
)



old_x = state.x



command.execute("RIGHT")



check(
    state.x == old_x + 1,
    "Input Command Changed World State"
)



command.execute("LEFT")



check(
    state.x == old_x,
    "Reverse Command Restored State"
)



command.execute("RESET")



check(
    state.x == 0,
    "Reset System Works"
)



print("\n" + "=" * 40)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")



if failed == 0:
    print("\n🟢 TRIOS CORE SYSTEM HEALTHY")
else:
    print("\n🔴 TRIOS CORE SYSTEM NEEDS FIX")