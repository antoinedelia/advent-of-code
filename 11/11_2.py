from dataclasses import dataclass, field
from math import floor
import heapq
from functools import reduce
import operator
import re


MAP_OPERATION = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


@dataclass
class Item:
    worry_level: int

    def operation(self, operator: str, b: int = 0):
        if b == 0:
            b = self.worry_level
        self.worry_level = MAP_OPERATION[operator](self.worry_level, b)

    def monkey_bored(self, modulo: int = 0):
        self.worry_level = self.worry_level % modulo

    def test(self, divisible_by: int) -> bool:
        return self.worry_level % divisible_by == 0


@dataclass
class Monkey:
    id: int
    divisible_by: int = None
    next_monkey_id_if_true: int = None
    next_monkey_id_if_false: int = None
    operator: str = None
    operation_number: str = None
    number_of_inspections: int = 0
    items: list[Item] = field(default_factory=list)

    def get_next_monkey(self, condition: bool):
        return self.next_monkey_id_if_true if condition else self.next_monkey_id_if_false


with open("11/11_input.txt") as f:
    input = f.read()

monkeys: list[Monkey] = []
for i, monkey in enumerate(input.split("\n\n")):
    new_monkey = Monkey(i)
    for j, line in enumerate(monkey.split("\n")):
        if j == 0:
            new_monkey.id = int(line[-2:-1])
        if j == 1:
            new_monkey.items = [Item(int(s)) for s in re.findall(r"\b\d+\b", line)]
        if j == 2:
            new_monkey.operator = [s for s in line if s in MAP_OPERATION.keys()][0]
            new_monkey.operation_number = int("".join([s for s in re.findall(r"\b\d+\b", line)]) or 0)
        if j == 3:
            new_monkey.divisible_by = [int(s) for s in re.findall(r"\b\d+\b", line)][0]
        if j == 4:
            new_monkey.next_monkey_id_if_true = [int(s) for s in re.findall(r"\b\d+\b", line)][0]
        if j == 5:
            new_monkey.next_monkey_id_if_false = [int(s) for s in re.findall(r"\b\d+\b", line)][0]
    monkeys.append(new_monkey)

modulo = 1
for i in [m.divisible_by for m in monkeys]:
    modulo *= i

for _ in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.number_of_inspections += 1
            item.operation(monkey.operator, monkey.operation_number)
            item.monkey_bored(modulo)
            condition = item.test(monkey.divisible_by)
            next_monkey = monkey.get_next_monkey(condition)
            receiver = [monkey for monkey in monkeys if monkey.id == next_monkey][0]
            receiver.items.append(item)
            monkey.items = [i for i in monkey.items if i is not item]

for monkey in monkeys:
    print(f"Monkey inspected items {monkey.number_of_inspections} times.")

result = reduce(operator.mul, heapq.nlargest(2, [m.number_of_inspections for m in monkeys]), 1)
print(result)
