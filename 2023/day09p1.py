from itertools import pairwise

x = [list(map(int, l.split())) for l in open(0).read().splitlines()]

tot = 0

for l in x:
    histories = []
    has_history = True
    histories.append(l)
    while has_history:
        temp = []
        for a, b in pairwise(histories[-1]):
            temp.append(b - a)
        histories.append(temp)
        if histories[-1].count(0) == len(histories[-1]):
            has_history = False
            break
    tot += sum(h[-1] for h in histories)

print(tot)
