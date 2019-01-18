import wpilib
import ctre
from Elevator import Elevator
from magicbot import StateMachine, state, timed_state

class ElevatorControl(StateMachine):

    elevator : Elevator

    def move_elevator(self, position):
        self.engage()
        pass

    @state
    def bottom_elevator(self):
        pass

    @state
    def middle_elevator(self):
        pass
    
    @state
    def top_elevator(self):
        pass