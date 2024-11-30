# Represents a generic neuron with basic properties and functions common to all neuron types.
class Neuron:
    def __init__(self, firing_rate: int):
        self.firing_rate = firing_rate

    def activate(self, stimulus: str):
        pass
