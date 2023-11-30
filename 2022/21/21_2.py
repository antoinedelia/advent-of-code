import re
from sympy.solvers import solve
from sympy import Symbol

IS_TEST = False

var_done = set()

with open("21/21_test_input.txt" if IS_TEST else "21/21_input.txt") as f:
    infos = f.read().splitlines()

for info in infos:
    if info[:4] == "root":
        root_end = info.split("root: ")[1].replace("+", "==")
        break

while True:
    for info in infos:
        name = info[:4]
        if name == "humn":
            continue
        if name in root_end:
            equation = info.split(": ")[1]
            root_end = root_end.replace(name, f"({equation})")
    result = re.findall(r"[\w]{4}", root_end)
    if "humn" in root_end and len(result) == 1 and result[0] == "humn":
        break

x = Symbol("humn")

left, right = root_end.split(" == ")
r = f"{left} - {right}"
print(solve(r, x)[0])
