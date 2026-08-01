# Known vs Unknown Environment

class Agent:
    def known(self):
        print("Known Environment")
        print("Agent knows all actions and outcomes.")

    def unknown(self):
        print("Unknown Environment")
        print("Agent learns through experience.")

agent = Agent()
agent.known()
agent.unknown()
