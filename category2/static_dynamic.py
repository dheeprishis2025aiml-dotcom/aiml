# Static vs Dynamic Environment

import time

print("Static Environment")
number = 10
print("Value:", number)

print("\nDynamic Environment")
for i in range(5):
    print("Changing Value:", i)
    time.sleep(1)
