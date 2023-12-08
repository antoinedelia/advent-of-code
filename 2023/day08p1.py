import re

x = open(0).read()

start = "AAA"
end = "ZZZ"

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

current = start
number_of_steps = 0

while True:
    for command in commands:
        current = map_paths[current][command]
        number_of_steps += 1
        if current == end:
            print(number_of_steps)
            exit(0)
