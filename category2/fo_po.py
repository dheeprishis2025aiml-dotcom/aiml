# Fully Observable vs Partially Observable

class Environment:
    def __init__(self):
        self.rooms = {"A": "Clean", "B": "Dirty"}

    def fully_observable(self):
        print("Fully Observable Environment")
        print(self.rooms)

    def partially_observable(self):
        print("Partially Observable Environment")
        print({"A": self.rooms["A"]})

env = Environment()
env.fully_observable()
env.partially_observable()
