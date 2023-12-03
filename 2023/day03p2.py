x = open(0).read()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

table = []
for l in x.splitlines():
    table.append([c for c in l])

gears_pos = {}

for row, l in enumerate(x.splitlines()):
    current_digit = ""
    valid_digit = False
    current_gear = None
    for col, c in enumerate(l):
        # we check if the previous number we looked is over and valid
        if not c.isdigit() and current_digit and valid_digit:
            if current_gear not in gears_pos:
                gears_pos[current_gear] = []
            gears_pos[current_gear].append(int(current_digit))
            current_digit = ""
            valid_digit = False
            continue
        if not c.isdigit() and current_digit and not valid_digit:
            current_digit = ""
            valid_digit = False
            continue
        if c.isdigit():
            current_digit += c
            for dx, dy in dirs:
                new_x = row + dx
                new_y = col + dy
                try:
                    if table[new_x][new_y] == "*":
                        current_gear = new_x + new_y * 1j
                        valid_digit = True
                except:
                    # out of bounds
                    pass

tot = 0
for k, v in gears_pos.items():
    if len(v) == 2:
        tot += v[0] * v[1]
print(tot)
