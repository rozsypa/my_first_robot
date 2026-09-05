#first review exercise of python programming

while True:

    distance = input("zadej hodnotu: ")

    try:
        distance = float(distance)

    except ValueError:

        print("spatne zadano")
        continue

    if distance < 0:
        state = "invalid input"

    elif distance <0.4:
        state = "STOP"

    elif 0.4 >=distance < 1:
        state = "SLOW"

    elif distance >= 1:
        state = "GO"

    else:
        state = "invalid input"

    print(state)
