##tady vytvorime class motor, ktera morotu prideli atributy name, speed a enabled
##jako metody pouzijeme start, stop, set_speed

class Motor:
    def __init__(self,name):
        self.name = name
        self.speed = 0
        self.enabled = False
        self.max_speed = 0
    def start(self):
        self.enabled = True

    def stop(self):
        self.enabled = False
        self.speed = 0

    def set_speed(self,speed):
        self.speed = speed

        


motor = Motor("left")           ## tady jen deklarujeme objekt. dostane name, ale enabled je False a speed = 0

print(motor.name, motor.speed, motor.enabled)
motor.start()
motor.set_speed(3)
                                ## tady jsme nastartovali, tzn. motor je enabled = True a nastavili jsem speed = 3
print(motor.name, motor.speed, motor.enabled)

motor.stop()
                                ## tady se motory zastavily - enabled = False a speed = 0
print(motor.name, motor.speed, motor.enabled)