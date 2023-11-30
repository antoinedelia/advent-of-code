from dataclasses import dataclass, field
from math import hypot

with open("09/09_test_input.txt") as f:
    motions = f.read().splitlines()


@dataclass
class Point:
    x: int
    y: int


def add_tail_to_visited_points(tail: Point):
    if (tail.x, tail.y) not in visited_points:
        visited_points.append((tail.x, tail.y))


@dataclass
class Grid:
    grid: list = field(default_factory=list)
    enabled: bool = True

    def __init__(self, grid=None, enabled: bool = True) -> None:
        self.reset_grid()
        self.enabled = enabled

    def reset_grid(self):
        self.grid = []
        for _ in range(6):
            new_list = []
            for _ in range(6):
                new_list.append(".")
            self.grid.append(new_list)

    def update_and_print_grid(self, start: Point, head: Point, tail: Point):
        if not self.enabled:
            return
        self.reset_grid()
        for visited_point in visited_points:
            self.grid[visited_point[1]][visited_point[0]] = "#"
        self.grid[start.y][start.x] = "s"
        self.grid[tail.y][tail.x] = "T"
        self.grid[head.y][head.x] = "H"
        # self.print_grid()

    def print_grid(self):
        if not self.enabled:
            return
        for line in self.grid[::-1]:
            print(line)
        print()


start = Point(0, 0)
head = Point(0, 0)
tail = Point(0, 0)
grid = Grid()

visited_points = []
add_tail_to_visited_points(tail)
grid.update_and_print_grid(start, head, tail)

for motion in motions:
    direction = motion.split()[0]
    number_of_steps = int(motion.split()[1])
    if direction == "R":
        for i in range(number_of_steps):
            head.x += 1
            dist = hypot(head.x - tail.x, head.y - tail.y)
            if dist == 2.0:
                tail.x += 1
                add_tail_to_visited_points(tail)
            if dist > 2.0:  # Move diagonally
                tail.x += 1
                tail.y = tail.y + 1 if head.y > tail.y else tail.y - 1
                add_tail_to_visited_points(tail)
            grid.update_and_print_grid(start, head, tail)
    if direction == "L":
        for i in range(number_of_steps):
            head.x -= 1
            dist = hypot(head.x - tail.x, head.y - tail.y)
            if dist == 2.0:
                tail.x -= 1
                add_tail_to_visited_points(tail)
            if dist > 2.0:  # Move diagonally
                tail.x -= 1
                tail.y = tail.y + 1 if head.y > tail.y else tail.y - 1
                add_tail_to_visited_points(tail)
            grid.update_and_print_grid(start, head, tail)
    if direction == "U":
        for i in range(number_of_steps):
            head.y += 1
            dist = hypot(head.x - tail.x, head.y - tail.y)
            if dist == 2.0:
                tail.y += 1
                add_tail_to_visited_points(tail)
            if dist > 2.0:  # Move diagonally
                tail.y += 1
                tail.x = tail.x + 1 if head.x > tail.x else tail.x - 1
                add_tail_to_visited_points(tail)
            grid.update_and_print_grid(start, head, tail)
    if direction == "D":
        for i in range(number_of_steps):
            head.y -= 1
            dist = hypot(head.x - tail.x, head.y - tail.y)
            if dist == 2.0:
                tail.y -= 1
                add_tail_to_visited_points(tail)
            if dist > 2.0:  # Move diagonally
                tail.y -= 1
                tail.x = tail.x + 1 if head.x > tail.x else tail.x - 1
                add_tail_to_visited_points(tail)
            grid.update_and_print_grid(start, head, tail)

grid.print_grid()
print(len(visited_points))
