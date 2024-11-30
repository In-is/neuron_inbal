# A motor neuron that controls muscle spindles, helping regulate muscle tone.
from motor import Motor


class GammaMotor(Motor):
    def __init__(self, firing_rate: int):
        super().__init__("muscle_spindle", firing_rate)

    def control_muscle(self, activation_level: int) -> None:
        pass
