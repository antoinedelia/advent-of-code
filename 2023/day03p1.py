x = open(0).read()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

table = []
for l in x.splitlines():
    table.append([c for c in l])

valid_numbers = []

for row, l in enumerate(x.splitlines()):
    current_digit = ""
    valid_digit = False
    for col, c in enumerate(l):
        # we check if the previous number we looked is over and valid
        if not c.isdigit() and current_digit and valid_digit:
            valid_numbers.append(int(current_digit))
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
                    if table[new_x][new_y] != "." and not table[new_x][new_y].isdigit():
                        valid_digit = True
                except:
                    # out of bounds
                    pass
    if current_digit and valid_digit:
        valid_numbers.append(int(current_digit))

print(sum(valid_numbers))
