x = open(0).read().split(",")

tot = []

for sequence in x:
    current = 0
    for c in sequence:
        current += ord(c)
        current *= 17
        current %= 256
    tot.append(current)
print(sum(tot))
