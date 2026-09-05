##tohle provede spojeni funkci calculate_speed a calculate_wheel_speed.
##dosadime tri vstupni promenne distance, track_width, omega ->rychlost ->left, right
from calculate_speed import calculate_speed
from calculate_wheel_speed import calculate_wheel_speeds


distance = 0.75
track_width = 0.30
omega = 0.0

speed = calculate_speed(distance)
wheel_speed = calculate_wheel_speeds(speed,omega,track_width)

left,right = wheel_speed

print(f"Distance: {distance} m")
print(f"Target speed: {speed} m/s")
print(f"left wheel: {left} m/s")
print(f"Right wheel: {right} m/s")