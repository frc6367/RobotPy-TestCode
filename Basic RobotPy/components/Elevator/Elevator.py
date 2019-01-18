import wpilib
import ctre

class Elevator:
    motor : ctre.WPI_TalonSRX

    
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def set_speed(self, motor_speed):
        if(self.enabled is True):
            self.motor.set_speed(motor_speed)
        else:
            self.motor.set_speed(0)
