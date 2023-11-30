from dataclasses import dataclass
from math import hypot

with open("09/09_input.txt") as f:
    motions = f.read().splitlines()


@dataclass
class Point:
    x: int
    y: int


X_START = 50
Y_START = 50

start = Point(X_START, Y_START)


def add_tail_to_visited_points(tail: Point):
    if (tail.x, tail.y) not in visited_points:
        visited_points.append((tail.x, tail.y))


last_ten_points = [Point(X_START, Y_START) for _ in range(10)]

visited_points = []
add_tail_to_visited_points(last_ten_points[-1])


def update_point_coords(point: Point, last_ten_points: list[Point]):
    previous_point = last_ten_points[num - 1]
    dist = hypot(previous_point.x - point.x, previous_point.y - point.y)
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
                update_point_coords(point, last_ten_points)
            add_tail_to_visited_points(last_ten_points[-1])
    if direction == "L":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.x -= 1
                    continue
                update_point_coords(point, last_ten_points)
            add_tail_to_visited_points(last_ten_points[-1])
    if direction == "U":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.y += 1
                    continue
                update_point_coords(point, last_ten_points)
            add_tail_to_visited_points(last_ten_points[-1])
    if direction == "D":
        for i in range(number_of_steps):
            for num, point in enumerate(last_ten_points):
                if num == 0:
                    point.y -= 1
                    continue
                update_point_coords(point, last_ten_points)
            add_tail_to_visited_points(last_ten_points[-1])

print(len(visited_points))
