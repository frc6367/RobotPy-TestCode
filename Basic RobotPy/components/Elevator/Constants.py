import wpilib
import ctre
from Gains import Gains

class Constants:

    kSlotIdx = 0
    kPIDLoopIdx = 0
    kTimeoutMs = 30
    kGains : Gains

    def __init__(self):
        self.kGains.__init__(0.2, 0.0, 0.0, 0.2, 0, 1.0)