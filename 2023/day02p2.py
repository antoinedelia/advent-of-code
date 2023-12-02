import re
from functools import reduce

x = open(0).read()

t = 0


for i, l in enumerate(x.splitlines(), 1):
    map_color_min = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    sets = l.split(": ")[1].split("; ")
    for set in sets:
        for draw in set.split(", "):
            for color, min_value in map_color_min.items():
                if color in draw and int(re.findall(r"\d+", draw)[0]) > min_value:
                    map_color_min[color] = int(re.findall(r"\d+", draw)[0])
    t += reduce(lambda x, y: x * y, map_color_min.values())

print(t)
