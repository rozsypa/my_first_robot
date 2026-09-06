##pridame atribut max speed. v pripade zadani vyssi rychlosti bude vysledna rychlost
##stale jen ta maximalni povolena

class Motor:
    def __init__(self,name):
        self.name = name
        self.speed = 0
        self.enabled = False
        self.max_speed = 15

    def start(self):
        self.enabled = True

    def stop(self):
        self.enabled = False
        self.speed = 0

    def set_speed(self,speed):
        if -self.max_speed <= speed <= self.max_speed:
            self.speed = speed
        elif -self.max_speed > speed:
            self.speed = -self.max_speed
        else:
            self.speed = self.max_speed




