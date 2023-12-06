import re
from functools import reduce

x = open(0).read().splitlines()

time = int("".join(list(re.findall(r"\d+", x[0]))))
distance = int("".join(list(re.findall(r"\d+", x[1]))))

number_of_records = []

dists = []
for time_button_held in range(time):
    boat_speed = time_button_held
    current_distance = boat_speed * (time - time_button_held)
    if current_distance > distance:
        dists.append(current_distance)
number_of_records.append(len(dists))

print(reduce(lambda x, y: x * y, number_of_records))
