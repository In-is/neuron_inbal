# A motor neuron that controls skeletal muscles.
from motor import Motor


class AlphaMotor(Motor):
    def __init__(self, firing_rate: int):
        super().__init__("skeletal muscle", firing_rate)

    def control_muscle(self, activation_level: int) -> None:
        pass
