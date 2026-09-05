#tohle bude pocitat rychlost jednotlivych kol pro diferencialni podvozek

def calculate_wheel_speeds(v, omega, track_width):
    left = v-omega*track_width/2
    right = v+omega*track_width/2

    return left,right
# forward drive (vr = vl, v = 1, omega = 0, track_width = 0.3)
# rotation on spot (vr = -vl, v = 0, omega = 1, track_width = 0.3)
# turning (vr =/= vl, v = 0.5, omega = 0.6, track_width = 0.3)
