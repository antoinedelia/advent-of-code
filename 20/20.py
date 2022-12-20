from collections import deque

IS_TEST = False
IS_PART_ONE = False

with open("20/20_test_input.txt" if IS_TEST else "20/20_input.txt") as f:
    numbers = list(map(int, f.read().splitlines()))


def convert(num: int | str, index: str = None) -> str | int:
    if type(num) is int:
        return str(num) + "/" + str(index)
    else:
        return int(num.split("/")[0])


for i, n in enumerate(numbers):
    if n != 0:
        numbers[i] = convert(n if IS_PART_ONE else n * 811589153, i)

og_numbers = numbers[::]
q = deque(numbers)

for _ in range(1 if IS_PART_ONE else 10):
    for num in og_numbers:
        if num == 0:
            continue
        idx = q.index(num)
        q.rotate(-idx)
        q.popleft()
        q.rotate(-convert(num))
        q.insert(0, num)

result = 0

for i, n in enumerate(q):
    if n != 0:
        q[i] = convert(n)

for i in [1000, 2000, 3000]:
    r = (q.index(0) + i) % len(q)
    result += q[r]

print(result)
