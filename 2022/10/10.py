from dataclasses import dataclass


@dataclass
class Cycle:
    index: int
    during: int


with open("10/10_input.txt") as f:
    instructions = f.read().splitlines()

x = 1
cycle_number = 1

cycles: list[Cycle] = []

for instruction in instructions:
    cycle = Cycle(cycle_number, x)
    if instruction == "noop":
        cycles.append(cycle)
        cycle_number += 1
        continue
    num = int(instruction.split()[1])
    cycles.append(cycle)
    cycle_number += 1
    cycle = Cycle(cycle_number, x)
    cycles.append(cycle)
    x += num
    cycle_number += 1

CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220]

print(sum(c.during * c.index for c in cycles if c.index in CYCLES_TO_CHECK))

i = 0
for cycle in cycles:
    sprite_pos = [cycle.during - 1, cycle.during, cycle.during + 1]
    if i in sprite_pos:
        print("#", end="")
    else:
        print(".", end="")
    i += 1
    if cycle.index % 40 == 0:
        print()
        i = 0
