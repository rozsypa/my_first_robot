# this little lovely script is here to check the code with a handful of assert conditions
# mainly to satisfy my AI tutor, that keeps piling up assignments to drive me crazy

from robot import Robot
from robot_states import RobotState
from motor_safe import Motor

terminator = Robot()
assert terminator.state == RobotState.STOPPED
terminator.start()
assert terminator.state == RobotState.RUNNING
terminator.emergency_stop()
assert terminator.state == RobotState.EMERGENCY
assert terminator.left_motor.enabled == False
terminator.reset()
assert terminator.state == RobotState.STOPPED
terminator.update("d")
assert terminator.state == RobotState.EMERGENCY
terminator.reset()
terminator.drive(3,"d")
assert terminator.state == RobotState.EMERGENCY
terminator.reset()
terminator.update(0.5)
terminator.start()
terminator.drive(1,0)
print(terminator.left_motor_speed)
print(terminator.max_speed)
assert terminator.left_motor_speed == terminator.max_speed
