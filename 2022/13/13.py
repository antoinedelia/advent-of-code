import ast
from itertools import zip_longest

with open("13/13_input.txt") as f:
    pair_input = f.read()

right_order_pairs = []


def is_in_right_order(pair_one: int | list, pair_two: int | list) -> bool:
    for first, second in zip_longest(pair_one, pair_two, fillvalue=-1):
        if first == -1:
            return True
        if second == -1:
            return False
        if type(first) is list and type(second) is list:
            result = is_in_right_order(first, second)
            if result is not None:
                return result
        elif type(first) is not type(second):
            if type(first) is not list:
                first = [first]
            else:
                second = [second]
            result = is_in_right_order(first, second)
            if result is not None:
                return result
        else:
            if first < second:
                return True
            if first > second:
                return False
    return None


for i, pairs in enumerate(pair_input.split("\n\n"), start=1):
    pair_one, pair_two = (ast.literal_eval(pair) for pair in pairs.splitlines())
    if is_in_right_order(pair_one, pair_two):
        right_order_pairs.append(i)

print(sum(right_order_pairs))


final_list = []


def add_to_list(pair: list):
    if not final_list:
        final_list.append(pair)
        return
    for i, item in enumerate(final_list):
        if is_in_right_order(pair, item):
            final_list.insert(i, pair)
            return i + 1
    final_list.append(pair)


for i, pairs in enumerate(pair_input.split("\n\n"), start=1):
    pair_one, pair_two = (ast.literal_eval(pair) for pair in pairs.splitlines())
    add_to_list(pair_one)
    add_to_list(pair_two)

print(add_to_list([[2]]) * add_to_list([[6]]))
