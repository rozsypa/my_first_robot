#this fail contains possible system states, limiting system functions
# for safety reasons
from enum import Enum


class RobotState(Enum):
    RUNNING=1
    STOPPED=2
    EMERGENCY=3







