# Discrete vs Continuous Environment

print("Discrete Environment")
states = ["Start", "Middle", "End"]
for state in states:
    print(state)

print("\nContinuous Environment")
position = 0.0
while position <= 1.0:
    print(round(position, 1))
    position += 0.2
