import re

x = open(0).read()

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

t = 0
for l in x.splitlines():
    indexes = {}
    ind = []
    for num, value in numbers.items():
        if num in l:
            indices = [m.start() for m in re.finditer(num, l)]
            ind.extend(indices)
            for i in indices:
                indexes[i] = value
    t += int(indexes[min(ind)] + indexes[max(ind)])

print(t)
