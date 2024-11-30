# A neuron that detects and responds to external stimuli. Each sensory neuron is sensitive to a specific type of stimulus, such as light or pressure.
from neuron import Neuron


class Sensory(Neuron):
    def __init__(self, receptor_type: str, firing_rate: int) -> None:
        super().__init__(firing_rate)
        self.receptor_type = receptor_type

    def sense_stimulus(self, stimulus: int) -> None:
        pass
