import re

x = open(0).read()

ids = []

map_color_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for i, l in enumerate(x.splitlines(), 1):
    is_possible = True
    sets = l.split(": ")[1].split("; ")
    for set in sets:
        for draw in set.split(", "):
            for color, max_value in map_color_max.items():
                if color in draw and int(re.findall(r"\d+", draw)[0]) > max_value:
                    is_possible = False
    if is_possible:
        ids.append(i)

print(sum(ids))
