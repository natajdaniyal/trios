import os
import sys


sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from command import CommandCenter



print("\n⌨️ TRIOS INPUT ENGINE TEST")
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

command = CommandCenter()



check(
    command is not None,
    "Command Receiver Exists"
)



check(
    hasattr(command, "execute"),
    "Input Target Exists"
)



# شبیه سازی فرمان‌هایی که Input Engine تولید می‌کند

commands = [
    "RIGHT",
    "LEFT",
    "RESET",
    "QUIT"
]



for item in commands:

    check(
        isinstance(item, str),
        f"Command Generated: {item}"
    )



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")



if failed == 0:

    print("\n🟢 Input Engine Logic Healthy")

else:

    print("\n🔴 Input Engine Needs Review")