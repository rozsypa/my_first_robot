#tohle bude funkce, ktera na zaklade vstupu distance nastavi rychlost

from robot_states import RobotState

def calculate_speed(distance):
#je idealni nejprve osetrit neplatne vstupy. vystup je mozne deklarovat rovnou v podminkach. neni treba
#delat dalsi promennou

    if isinstance(distance,(int,float)):
        if distance <=0:
            return 0.0

        elif distance <=0.4:
            return 0.0

        elif distance <1:
            return 0.2

        elif distance >=1:
            return 0.5

    else:
        return None


