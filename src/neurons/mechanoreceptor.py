# A sensory neuron that responds to pressure
from sensory import Sensory


class Mechanoreceptor(Sensory):
    def __init__(self, firing_rate: int):
        super().__init__("pressure", firing_rate)

    def sense_stimulus(self, pressure: int) -> None:
        pass
