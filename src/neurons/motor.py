# A neuron responsible for initiating muscle movement by sending activation signals to a target muscle

from neuron import Neuron


class Motor(Neuron):
    def __init__(self, target_muscle: str, firing_rate: int) -> None:
        super().__init__(firing_rate)
        self.target_muscle = target_muscle

    def control_muscle(self, activation_level: int) -> None:
        pass
