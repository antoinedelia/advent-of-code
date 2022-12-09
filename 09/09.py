from dataclasses import dataclass
from math import hypot

with open("09/09_input.txt") as f:
    motions = f.read().splitlines()


@dataclass
class Point:
    x: int
    y: int


def add_tail_to_visited_points(tail: Point):
    if (tail.x, tail.y) not in visited_points:
        visited_points.append((tail.x, tail.y))


start = Point(0, 0)
head = Point(0, 0)
tail = Point(0, 0)

visited_points = []
add_tail_to_visited_points(tail)

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

print(len(visited_points))
