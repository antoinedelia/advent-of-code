import re
from copy import deepcopy

with open("05/05_input.txt") as f:
    infos = f.read().splitlines()

stacks = {}

for info in infos:
    if not info:
        break
    line = [info[i : i + 4].replace(" ", "") for i in range(0, len(info), 4)]
    for i, item in enumerate(line, 1):
        if item.isdigit():
            break
        if i not in stacks:
            stacks[i] = []
        if item:
            stacks[i].insert(0, item)

stacks_part_two = deepcopy(stacks)

for j, info in enumerate(infos):
    if not info.startswith("move"):
        continue

    amount, first_position, last_position = [int(s) for s in re.findall(r"\b\d+\b", info)]
    items_to_move = [item for item in stacks[first_position] if item][::-1][:amount]
    stacks[last_position].extend(items_to_move)
    stacks[first_position] = stacks[first_position][: len(stacks[first_position]) - amount]

    items_to_move_part_two = [item for item in stacks_part_two[first_position] if item][::-1][:amount][::-1]
    stacks_part_two[last_position].extend(items_to_move_part_two)
    stacks_part_two[first_position] = stacks_part_two[first_position][: len(stacks_part_two[first_position]) - amount]


print("".join([v[-1] for v in stacks.values()]).replace("[", "").replace("]", ""))
print("".join([v[-1] for v in stacks_part_two.values()]).replace("[", "").replace("]", ""))
