import re
from math import dist

IS_TEST = False

with open("15/15_test_input.txt" if IS_TEST else "15/15_input.txt") as f:
    infos = f.read().splitlines()
y = 10 if IS_TEST else 2000000

t = set()
beacons_to_remove = set()

for info in infos:
    sx, sy, bx, by = re.findall(r"-?\d+", info)
    sx, sy = (int(sx), int(sy))
    bx, by = (int(bx), int(by))

    new_x = abs(sx - bx) + abs(sy - by)
    new_x -= abs(y - sy)

    xmin = -new_x + sx
    xmax = new_x + sx

    if by == y:
        beacons_to_remove.add((bx, by))

    for x in range(xmin, xmax + 1):
        if dist((sx, sy), (x, y)) <= dist((sx, sy), (bx, by)):
            t.add((x, y))

print(len(t) - len(beacons_to_remove))
