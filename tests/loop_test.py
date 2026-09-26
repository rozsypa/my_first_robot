#timer

import time

previous_time = None

def control_callback():
    global previous_time
    current_time = time.perf_counter()

    if previous_time is None:
        previous_time = current_time
        return previous_time

    else:
        diff = current_time - previous_time
        previous_time = current_time

        return diff



print(control_callback())
time.sleep(0.5)
print(control_callback())
time.sleep(0.5)
print(control_callback())
time.sleep(0.5)
print(control_callback())
time.sleep(0.5)
print(control_callback())


