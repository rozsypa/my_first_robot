##kombinace tridy motor, calculate_speed and calculate_wheel_speed


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

    def _set_state(self, new_state):

        if self.state != RobotState.EMERGENCY and new_state == RobotState.RUNNING:
            self.state = new_state
            self.left_motor.start()  ##nastartuje motory, pokud je state RUNNING. Pokud je cokoli jineho
            self.right_motor.start()

        elif new_state == RobotState.STOPPED:
            self.state = new_state
            self.left_motor.stop()
            self.right_motor.stop()

        elif new_state == RobotState.EMERGENCY:
            self.state = new_state
            self.left_motor.stop()
            self.right_motor.stop()

    def start(self):
        if self.state == RobotState.STOPPED:
            self._set_state(RobotState.RUNNING)         ##nastartuje motory, pokud je state RUNNING. Pokud je cokoli jineho
                                                                    ##motor nenaskoci

    def stop(self):
        if self.state == RobotState.RUNNING:
            self._set_state(RobotState.STOPPED)                ## prepne jakykoliv state do stavu STOPPED, pokud je running


    def emergency_stop(self):                   ## prepne jakykoliv state do state emergency
        self._set_state(RobotState.EMERGENCY)


    def reset(self):
        self._set_state(RobotState.STOPPED)

    def update(self,distance):

        new_max_speed = calculate_speed(distance) #definuje max rychlost fci vzdalenosti

        if new_max_speed is None:
            self._set_state(RobotState.EMERGENCY)

        else:
            self.max_speed = new_max_speed

    def drive(self,v,omega):#definuje rychlosti jednotlivych motoru
        if isinstance(v,(int,float)) and isinstance(omega,(int,float)):

            if self.state == RobotState.RUNNING:

                if abs(v)<= self.max_speed:

                    safe_v = v

                else:
                    if v<0:
                        safe_v = -self.max_speed

                    else:
                        safe_v = self.max_speed

                self.left_motor_speed, self.right_motor_speed = calculate_wheel_speeds(safe_v, omega, track_width=0.3)
                self.left_motor.set_speed(self.left_motor_speed)
                self.right_motor.set_speed(self.right_motor_speed)

        else:
            self._set_state(RobotState.EMERGENCY)








#print(eniac.left_motor.speed,eniac.right_motor.speed,eniac.max_speeniac.motor_left_speeded,eniac.left_motor.enabled, eniac.right_motor.enabled)