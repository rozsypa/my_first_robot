#tenhle kod projde data ze senzoru v listu data a najde minimalni hodnotu.
# Pokud tam bude hodnota None, bude ji ignorovat

measurements = [
    1.4,
    0.9,
    None,
    0.62,
    0.31,
    None,
    1.8
]

valid_measurements = []

for reading in measurements:
    if isinstance(reading, float):
        valid_measurements.append(reading)           #nemenit list behem iterace!!!
    else:
        continue

print(f"nearest obstacle is {min(valid_measurements)} m")


