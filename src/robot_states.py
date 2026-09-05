#this fail contains possible system states, limiting system functions
# for safety reasons
from enum import Enum


class RobotState(Enum):
    RUNNING=1
    STOPPED=2
    EMERGENCY=3

def set_states(self,new_state):
    self.state = new_state

    if new_state == RobotState.RUNNING:
        self.left_motor.start()  ##nastartuje motory, pokud je state RUNNING. Pokud je cokoli jineho
        self.right_motor.start()

    if new_state == RobotState.STOPPED:
        self.left_motor.stop()
        self.right_motor.stop()

    if new_state == RobotState.EMERGENCY:
        self.left_motor.stop()
        self.right_motor.stop()





