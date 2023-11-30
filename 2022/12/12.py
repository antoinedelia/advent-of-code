import collections
from string import ascii_lowercase

MAP_LETTER_NUMBER = {}
for i, letter in enumerate(ascii_lowercase, start=1):
    MAP_LETTER_NUMBER[letter] = i
MAP_LETTER_NUMBER["S"] = 1
MAP_LETTER_NUMBER["E"] = 26


def can_move(current_letter: str, new_letter: str) -> bool:
    return MAP_LETTER_NUMBER[new_letter] <= MAP_LETTER_NUMBER[current_letter] + 1


def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set()
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and can_move(grid[y][x], grid[y2][x2]) and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


with open("12/12_input.txt") as f:
    map_input = f.read().splitlines()

for y, row in enumerate(map_input):
    for x, pixel in enumerate(row):
        if pixel == "S":
            start = (x, y)
            break

goal = "E"
width, height = len(map_input[0]), len(map_input)
path = bfs(map_input, start)
path.remove(start)
print(len(path))

# Part 2
possible_start_points = []
for y, row in enumerate(map_input):
    for x, pixel in enumerate(row):
        if pixel == "a":
            possible_start_points.append((x, y))

results = []
for start_point in possible_start_points:
    path = bfs(map_input, start_point)
    if not path:
        continue
    path.remove(start_point)
    results.append((len(path)))

print(min(results))
