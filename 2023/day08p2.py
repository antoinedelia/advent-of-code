import math
import re

x = open(0).read()

starts = []

map_dir = {
    "L": 0,
    "R": 1,
}

map_paths = {}

for i, l in enumerate(x.splitlines()):
    if i == 0:
        commands = list(l)
        continue
    if not l:
        continue

    current, left, right = re.findall(r"\w{3}", l)
    map_paths[current] = {
        "L": left,
        "R": right,
    }

starts = [path for path in map_paths.keys() if path[-1] == "A"]

steps = []

for start in starts:
    current = start
    number_of_steps = 0
    should_stop = False
    while not should_stop:
        for command in commands:
            current = map_paths[current][command]
            number_of_steps += 1
            if current[-1] == "Z":
                steps.append(number_of_steps)
                should_stop = True
                break

print(math.lcm(*steps))
