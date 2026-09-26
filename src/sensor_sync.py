#this is a small exercise to try a sensor sync for future sensor fusion
import math
#encoder data (timestamp, position)
encoder_data = [
    (1.00,0.50),
    (1.10,0.56)
]

camera_time = 1.01

#function return pos estimate of robot in camera_time

def interpolate_position(t1,x1,t2,x2,target_time):

    if math.isclose(t2-t1,0.0,rel_tol=1e-5,abs_tol=1e-5):

        return "error"
    elif target_time<= t1 or t2<=target_time:
        return "error extrapolace"

    else:
        x_t = ((target_time - t1) / (t2 - t1)) * (x2 - x1) + x1  # interpolation formula
        return x_t

print(interpolate_position(encoder_data[0][0],encoder_data[0][1],encoder_data[1][0],encoder_data[1][1],camera_time))