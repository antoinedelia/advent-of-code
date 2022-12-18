from itertools import combinations

IS_TEST = True

with open("18/18_test_input.txt" if IS_TEST else "18/18_input.txt") as f:
    squares = f.read()

cubes = []

for square in squares.splitlines():
    x, y, z = list(map(int, square.split(",")))
    cubes.append((x, y, z))

cubes = sorted(cubes)
total_unconnected_sides = len(cubes) * 6


for cube1, cube2 in combinations(cubes, 2):
    if (
        (cube1[0] == cube2[0] and cube1[1] == cube2[1] and abs(cube1[2] - cube2[2]) == 1)
        or (cube1[0] == cube2[0] and cube1[2] == cube2[2] and abs(cube1[1] - cube2[1]) == 1)
        or (cube1[1] == cube2[1] and cube1[2] == cube2[2] and abs(cube1[0] - cube2[0]) == 1)
    ):
        total_unconnected_sides -= 2


# Part 2 - Check for cubes trapped between other cubes - NOT WORKING
is_center = {}
for cube1, cube2 in combinations(cubes, 2):
    idx = cubes.index(cube1)
    if idx not in is_center:
        is_center[idx] = {}
        is_center[idx]["x"] = False
        is_center[idx]["y"] = False
        is_center[idx]["z"] = False
    if cube1[0] > cube2[0]:
        print(is_center)
        is_center[idx]["x"] = True
    if cube1[1] > cube2[1]:
        is_center[idx]["y"] = True
    if cube1[2] > cube2[2]:
        is_center[idx]["z"] = True


result = [k for k, v in is_center.items() if v["x"] is True and v["y"] is True and v["z"] is True]
for cube in result:
    total_unconnected_sides -= 6

print(total_unconnected_sides)
