import wpilib
import ctre

class Elevator:
    elevator_motor : ctre.WPI_TalonSRX

    
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def is_ready(self):
        # in a real robot, you'd be using an encoder to determine if the
        # shooter were at the right speed..
        return True

    def execute(self):
        '''This gets called at the end of the control loop'''
        if self.enabled:
            self.elevator_motor.set(1.0)
        else:
            self.elevator_motor.set(0)

        self.enabled = False