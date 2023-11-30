import re

IS_TEST = False

with open("15/15_test_input.txt" if IS_TEST else "15/15_input.txt") as f:
    infos = f.read().splitlines()


max_range = 20 if IS_TEST else 4000000

for y in range(max_range + 1):
    intervals = []

    for info in infos:
        sx, sy, bx, by = re.findall(r"-?\d+", info)
        sx, sy = (int(sx), int(sy))
        bx, by = (int(bx), int(by))

        distance = abs(sx - bx) + abs(sy - by)
        offset = distance - abs(y - sy)

        if offset < 0:
            continue

        xmin = sx - offset
        xmax = sx + offset
        intervals.append((xmin, xmax))

    intervals.sort()

    ranges = []

    for int_min, int_max in intervals:
        if not ranges:
            ranges.append([int_min, int_max])
            continue

        prev = ranges[-1]

        if int_min > prev[1] + 1:
            ranges.append([int_min, int_max])
            continue

        ranges[-1][1] = max(int_max, prev[1])

    if len(ranges) > 1:
        x = int((ranges[0][1] + ranges[1][0]) / 2)
        print(x, y)
        print(x * 4000000 + y)
        exit()
