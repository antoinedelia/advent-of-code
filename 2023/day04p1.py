x = open(0).read()

tot = []

for line in x.splitlines():
    numbers = line.split(": ")[1]
    win_numbers, my_numbers = [stack.split() for stack in numbers.split(" | ")]
    matching_numbers = set(win_numbers) & set(my_numbers)
    if matching_numbers:
        tot.append(2 ** (len(matching_numbers) - 1))

print(sum(tot))
