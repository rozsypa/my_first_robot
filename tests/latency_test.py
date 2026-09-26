#this is just a small script to calculate latency
#latency is difference between callback_time and measurement_time
import math
def latency_count(t_measurement,t_callback):
#t_measurement je timestamp hodnoty,
#t_callback je kdy ji zacne callback spracovavat

    if t_callback is None or t_measurement is None:
        return None
    else:
        latency = round(t_callback-t_measurement,3)
        return latency

def stopping_distance(latency,v):
    if latency is None or v is None:
        return None
    else:
        distance = round(v*latency,3)
        return distance

l=latency_count(10.00,10.05)
stopping_distance(l,0.5)

print(l,stopping_distance(l,0.5))


assert(math.isclose(latency_count(10.00,10.01),0.01))
assert(math.isclose(latency_count(10.00,10.05),0.05))
assert(math.isclose(latency_count(10.00,10.10),0.1))