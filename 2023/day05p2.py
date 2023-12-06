import re
import sys
from collections import defaultdict
from itertools import batched


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
        temp_seeds = list(map(int, re.findall(r"\d+", line)))
        for start, stop in batched(temp_seeds, 2):
            seeds.append((start, start + stop))

    if "map" in line:
        current_map = line.split()[0]
        continue

    if line[0].isdigit():
        destination_range_start, source_range_start, range_length = map(
            int, line.split()
        )
        if current_map not in map_map:
            map_map[current_map] = []
        map_map[current_map].append(
            (source_range_start, destination_range_start, range_length)
        )


paths_done = set()

first_seed_ranges = [(m[0], m[0] + m[2]) for m in map_map["seed-to-soil"]]

min_location = sys.maxsize
for start_seed, stop_seed in seeds:
    should_be_done = False
    for seed_range in first_seed_ranges:
        if stop_seed < seed_range[0] or start_seed > seed_range[1]:
            continue
        else:
            should_be_done = True
            break
    if not should_be_done:
        continue
    for seed in range(start_seed, stop_seed):
        new_path = f"{seed}-"
        last_number = seed
        if new_path in paths_done:
            continue
        for map_values in map_map.values():
            if new_path in paths_done:
                continue
            paths_done.add(new_path)
            for source, dest, map_range in map_values:
                if last_number in range(source, source + map_range):
                    last_number = last_number + (dest - source)
                    new_path += f"{last_number}-"
                    break
            new_path += f"{last_number}-"
        min_location = min(min_location, last_number)

print(min_location)
