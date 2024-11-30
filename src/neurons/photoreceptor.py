# A sensory neuron specifically sensitive to light
from sensory import Sensory


class Photoreceptor(Sensory):
    def __init__(self, firing_rate: int):
        super().__init__("light", firing_rate)

    def sense_stimulus(self, light_intensity: int) -> None:
        pass
