import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from state import state, TriosState


print("\n🧠 TRIOS STATE SYSTEM TEST")
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



check(
    isinstance(state, TriosState),
    "State Object Exists"
)


check(
    hasattr(state, "x"),
    "Position X Exists"
)


check(
    hasattr(state, "y"),
    "Position Y Exists"
)


old_x = state.x


state.move(10, 0)


check(
    state.x == old_x + 10,
    "State Movement Works"
)


state.reset()


check(
    state.x == 0 and state.y == 0,
    "State Reset Works"
)



print("\n" + "=" * 35)

print(f"✅ Passed : {passed}")
print(f"❌ Failed : {failed}")


if failed == 0:
    print("\n🟢 State System Healthy")
else:
    print("\n🔴 State System Has Problems")