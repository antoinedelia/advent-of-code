x = open(0).read()

t = 0
for l in x.splitlines():
    a, b = 0, 0
    for c in l:
        if c.isdigit():
            a = c
            break
    for c in l[::-1]:
        if c.isdigit():
            b = c
            break
    t += int(a + b)

print(t)
