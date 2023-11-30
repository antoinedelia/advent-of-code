from dataclasses import dataclass, field
from math import hypot

with open("09/09_input.txt") as f:
    motions = f.read().splitlines()


@dataclass
class Point:
    x: int
    y: int


GRID_SIZE = 100
X_START = 50
Y_START = 50

start = Point(X_START, Y_START)


@dataclass
class Grid:
    grid: list = field(default_factory=list)
    enabled: bool = True

    def __init__(self, grid=None, enabled: bool = True) -> None:
        self.reset_grid()
        self.enabled = enabled

    def reset_grid(self):
        self.grid = []
        for _ in range(GRID_SIZE):
            new_list = []
            for _ in range(GRID_SIZE):
                new_list.append(".")
            self.grid.append(new_list)

    def update_and_print_grid(self, points: list[Point]):
        if not self.enabled:
            return
        self.reset_grid()
        for visited_point in visited_points:
            self.grid[visited_point[1]][visited_point[0]] = "#"
        self.grid[start.y][start.x] = "s"
        for i, point in enumerate(points):
            self.grid[point.y][point.x] = str(i)
        self.grid[points[0].y][points[0].x] = "H"
        self.print_grid()

    def print_grid(self):
        if not self.enabled:
            return
        for line in self.grid[::-1]:
            print(line)
        print()


def add_tail_to_visited_points(tail: Point):
    if (tail.x, tail.y) not in visited_points:
        visited_points.append((tail.x, tail.y))


last_ten_points = [Point(X_START, Y_START) for _ in range(10)]

visited_points = []
add_tail_to_visited_points(last_ten_points[-1])

grid = Grid(enabled=False)
grid.update_and_print_grid(last_ten_points)


def update_point_coords(dist: float, point: Point, previous_point: Point):
    if dist == 2.0:
        if previous_point.x < point.x:
            point.x -= 1
        elif previous_point.y > point.y:
            point.y += 1
        elif previous_point.x > point.x:
            point.x += 1
        elif previous_point.y < point.y:
            point.y -= 1
    if dist > 2.0:  # Move diagonally
        point.x = point.x + 1 if previous_point.x > point.x else point.x - 1
        point.y = point.y + 1 if previous_point.y > point.y else point.y - 1


for motion in motions:
    direction = motion.split()[0]
    number_of_steps = int(motion.split()[1])
    if direction == "R":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.x += 1
                    continue
                previous_point = last_ten_points[num - 1]
                dist = hypot(previous_point.x - point.x, previous_point.y - point.y)
                update_point_coords(dist, point, previous_point)
            add_tail_to_visited_points(last_ten_points[-1])
        grid.update_and_print_grid(last_ten_points)
    if direction == "L":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.x -= 1
                    continue
                previous_point = last_ten_points[num - 1]
                dist = hypot(previous_point.x - point.x, previous_point.y - point.y)
                update_point_coords(dist, point, previous_point)
            add_tail_to_visited_points(last_ten_points[-1])
        grid.update_and_print_grid(last_ten_points)
    if direction == "U":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.y += 1
                    continue
                previous_point = last_ten_points[num - 1]
                dist = hypot(previous_point.x - point.x, previous_point.y - point.y)
                update_point_coords(dist, point, previous_point)
            add_tail_to_visited_points(last_ten_points[-1])
        grid.update_and_print_grid(last_ten_points)
    if direction == "D":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.y -= 1
                    continue
                previous_point = last_ten_points[num - 1]
                dist = hypot(previous_point.x - point.x, previous_point.y - point.y)
                update_point_coords(dist, point, previous_point)
            add_tail_to_visited_points(last_ten_points[-1])
        grid.update_and_print_grid(last_ten_points)

print(len(visited_points))
