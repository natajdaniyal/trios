import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from vector import Vector2


print("📐 TRIOS VECTOR TEST")
print("====================")


a = Vector2(3, 4)

print("Vector:", a)

print("Length:", a.length())


if a.length() == 5:
    print("✅ Vector Length Works")
else:
    print("❌ Vector Failed")


b = Vector2(1, 2)

c = a.add(b)

if c.x == 4 and c.y == 6:
    print("✅ Vector Addition Works")
else:
    print("❌ Addition Failed")


print("====================")
print("🟢 Vector System Healthy")