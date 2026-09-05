##kombinace tridy motor, calculate_speed and calculate_wheel_speed
from _dbus_bindings import String

from motor_safe import Motor
from calculate_wheel_speed import calculate_wheel_speeds
from calculate_speed import calculate_speed
from robot_states import RobotState


class Robot:
    def __init__(self):
        self.left_motor = Motor("left")     ##levy motor
        self.right_motor = Motor("right")   ##pravy motor
        self.max_speed = 0
        self.state = RobotState.STOPPED

    def set_state(self,new_state):
        self.state = new_state

    def start(self):
        if self.state == RobotState.STOPPED:

            self.set_state(RobotState.RUNNING)         ##nastartuje motory, pokud je state RUNNING. Pokud je cokoli jineho
                                                                    ##motor nenaskoci


    def stop(self):
        if self.state == RobotState.RUNNING:
            self.set_state(RobotState.STOPPED)                ## prepne jakykoliv state do stavu STOPPED, pokud je running


    def emergency_stop(self):                   ## prepne jakykoliv state do state emergency
        self.set_state(RobotState.EMERGENCY)


    def reset(self):
        self.set_state(RobotState.STOPPED)


    def update(self,distance):
        self.max_speed = calculate_speed(distance) #definuje max rychlost fci vzdalenosti

    def drive(self, v,omega):       #definuje rychlosti jednotlivych motoru
        if self.state == RobotState.RUNNING:

            if type(v)!=String:


                if v<= self.max_speed:

                    self.motor_left_speed, self.motor_right_speed = calculate_wheel_speeds(v,omega,track_width=0.3)

                else:
                    self.motor_left_speed, self.motor_right_speed = calculate_wheel_speeds(self.max_speed, omega, track_width=0.3)


            else:
                self.set_state(RobotState.EMERGENCY)    #chyba senzoru, hodnota None
                print("invalid distance input,sensor error")


            self.left_motor.set_speed(self.motor_left_speed)
            self.right_motor.set_speed(self.motor_right_speed)



eniac = Robot()
print(eniac.state)
eniac.start()
print(eniac.state)
eniac.emergency_stop()
print(eniac.state)
eniac.update(0.5)
print(eniac.state)
eniac.drive(2,0.4)
eniac.reset()
print(eniac.state)

#print(eniac.left_motor.speed,eniac.right_motor.speed,eniac.max_speeniac.motor_left_speeded,eniac.left_motor.enabled, eniac.right_motor.enabled)