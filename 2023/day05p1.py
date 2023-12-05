import re
import sys
from collections import defaultdict


def tree():
    return defaultdict(tree)


x = open(0).read()

seeds = []

map_map = tree()

current_map = None
for i, line in enumerate(x.splitlines()):
    if not line:
        current_map = None
        continue
    if i == 0:
        seeds = list(map(int, re.findall("\d+", line)))

    if "map" in line:
        current_map = line.split()[0]
        continue

    if line[0].isdigit():
        destination_range_start, source_range_start, range_length = map(int, line.split())
        if current_map not in map_map:
            map_map[current_map] = []
        map_map[current_map].append((source_range_start, destination_range_start, range_length))

min_location = sys.maxsize
for seed in seeds:
    last_number = seed
    for map_values in map_map.values():
        for source, dest, map_range in map_values:
            if last_number in range(source, source + map_range):
                last_number = last_number + (dest - source)
                break
    min_location = min(min_location, last_number)

print(min_location)
