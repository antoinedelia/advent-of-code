IS_TEST = False
with open("14/14_test_input.txt" if IS_TEST else "14/14_input.txt") as f:
    traces = f.read().splitlines()

cols_count = rows_count = 30 if IS_TEST else 1000
col_offset = 490 if IS_TEST else 0
row_offset = 0

sand_marker = "O"
wall_marker = "#"
empty_marker = "."

grid = [[empty_marker for x in range(cols_count)] for x in range(rows_count)]


def print_grid():
    if not IS_TEST:
        return
    for line in grid:
        print(line)
    print()


lowest_rock = 0
wall_placed = []

for trace in traces:
    prev_x = None
    prev_y = None
    for coords in trace.split(" -> "):
        x, y = coords.split(",")
        x: int = int(x) - col_offset
        y: int = int(y) - row_offset
        if x == prev_x:
            for i in range(abs(y - prev_y) + 1):
                if prev_y - y > 0:
                    grid[prev_y - i][x] = wall_marker
                else:
                    grid[prev_y + i][x] = wall_marker
        elif y == prev_y:
            for i in range(abs(x - prev_x) + 1):
                if prev_x - x > 0:
                    grid[y][prev_x - i] = wall_marker
                else:
                    grid[y][prev_x + i] = wall_marker
        else:
            grid[y][x] = wall_marker
        print_grid()
        prev_x = x
        prev_y = y
        if y > lowest_rock:
            lowest_rock = y

print_grid()
is_over = False
number_of_sand = 0
sand_placed = []

floor = lowest_rock

# PART 2 - comment out for part 1
floor = lowest_rock + 2
for x in range(rows_count):
    grid[floor][x] = wall_marker
# END OF PART 2

while not is_over:
    can_go_down = True
    sand_x = 500 - col_offset
    sand_y = 0 - row_offset
    grid[sand_y][sand_x] = sand_marker
    while can_go_down:
        if sand_y > floor:
            can_go_down = False
            continue
        if grid[sand_y + 1][sand_x] == empty_marker:
            grid[sand_y + 1][sand_x] = sand_marker
            grid[sand_y][sand_x] = empty_marker
            sand_y += 1
        elif grid[sand_y + 1][sand_x - 1] == empty_marker:
            grid[sand_y + 1][sand_x - 1] = sand_marker
            grid[sand_y][sand_x] = empty_marker
            sand_y += 1
            sand_x -= 1
        elif grid[sand_y + 1][sand_x + 1] == empty_marker:
            grid[sand_y + 1][sand_x + 1] = sand_marker
            grid[sand_y][sand_x] = empty_marker
            sand_y += 1
            sand_x += 1
        else:
            if (sand_y, sand_x) in sand_placed:
                can_go_down = False
                is_over = True
                break
            sand_placed.append((sand_y, sand_x))
            can_go_down = False
            number_of_sand += 1
    if sand_y > floor:
        is_over = True

print_grid()
print(number_of_sand)
print(len(sand_placed))
