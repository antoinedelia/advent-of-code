from functools import reduce

with open("08/08_input.txt") as f:
    grid = f.read().splitlines()

first_list = []
for line in grid:
    new_list = []
    for char in line:
        new_list.append(int(char))
    first_list.append(new_list)

second_list = [list(a) for a in zip(*first_list)]

visible_trees = []

# Left to right
for row_number, row in enumerate(first_list):
    biggest_tree = -1
    for col_number, tree in enumerate(row):
        coords = (col_number, row_number)
        if int(tree) > biggest_tree:
            if coords not in visible_trees:
                visible_trees.append(coords)
            biggest_tree = int(tree)

# Right to left
for row_number, row in enumerate(first_list):
    biggest_tree = -1
    for col_number, tree in reversed(list(enumerate(row))):
        coords = (col_number, row_number)
        if int(tree) > biggest_tree:
            if coords not in visible_trees:
                visible_trees.append(coords)
            biggest_tree = int(tree)

# Top to bottom
for col_number, col in reversed(list(enumerate(second_list))):
    biggest_tree = -1
    for row_number, tree in enumerate(col):
        coords = (col_number, row_number)
        if int(tree) > biggest_tree:
            if coords not in visible_trees:
                visible_trees.append(coords)
            biggest_tree = int(tree)

# Bottom to top
for col_number, row in reversed(list(enumerate(second_list))):
    biggest_tree = -1
    for row_number, tree in reversed(list(enumerate(row))):
        coords = (col_number, row_number)
        if int(tree) > biggest_tree:
            if coords not in visible_trees:
                visible_trees.append(coords)
            biggest_tree = int(tree)

print(len(visible_trees))

trees = {}
for i in range(len(first_list)):
    for j in range(len(first_list)):
        coords = (i, j)
        trees[coords] = []


def get_neighbors(coords: tuple) -> int:
    col = coords[0]
    row = coords[1]
    tree_value = second_list[col][row]
    # Going top
    top_score = 0
    for y in range(row - 1, -1, -1):
        top_score += 1
        neighbor_tree = second_list[col][y]
        if neighbor_tree >= tree_value:
            break

    # Going bottom
    bottom_score = 0
    for y in range(row + 1, len(second_list)):
        bottom_score += 1
        neighbor_tree = second_list[col][y]
        if neighbor_tree >= tree_value:
            break

    # Going left
    left_score = 0
    for x in range(col - 1, -1, -1):
        left_score += 1
        neighbor_tree = second_list[x][row]
        if neighbor_tree >= tree_value:
            break

    # Going right
    right_score = 0
    for x in range(col + 1, len(second_list)):
        right_score += 1
        neighbor_tree = second_list[x][row]
        if neighbor_tree >= tree_value:
            break

    return top_score * bottom_score * left_score * right_score


for tree in trees:
    value = get_neighbors(tree)
    trees[tree] = value

print(max(v for v in trees.values()))
