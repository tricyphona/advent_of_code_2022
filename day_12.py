import numpy as np
import math
import sys
with open("inputs/input_day12_0.txt", 'r') as f:
    lines = f.readlines()

test_input = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

# lines = test_input


class Point:
    corner_x, corner_y = len(lines[0]) - 1, len(lines) - 1

    def __init__(self, x, y, height, weight=math.inf):
        self.x = x
        self.y = y
        self.height = height
        self.weight = weight
        self.walkable_neighbours = None

    def available_paths(self):
        up, down, right, left = [False for i in range(4)]
        if self.y > 0 \
                and self.self_lower_weight(self.x, self.y - 1) \
                and self.check_walkable_height_difference(self.x, self.y - 1):
            up = True
        if self.y < Point.corner_y \
                and self.self_lower_weight(self.x, self.y + 1) \
                and self.check_walkable_height_difference(self.x, self.y + 1):
            down = True
        if self.x < Point.corner_x \
                and self.self_lower_weight(self.x + 1, self.y) \
                and self.check_walkable_height_difference(self.x + 1, self.y):
            right = True
        if self.x > 0 \
                and self.self_lower_weight(self.x - 1, self.y) \
                and self.check_walkable_height_difference(self.x - 1, self.y):
            left = True
        return up, down, right, left

    def check_walkable_height_difference(self, x, y):
        return heightmap[y][x].height - self.height <= 1

    def self_lower_weight(self, x, y):
        # print(f"weight: {self.weight}, other: {heightmap[y][x].weight}, coords: {x}, {y}")
        return self.weight < heightmap[y][x].weight

    def overwrite_weight(self, other):
        other.weight = self.weight + 1

    def get_walkable_neighbours(self, available_paths):
        up, down, right, left = available_paths
        objects_returned = []
        if up:
            objects_returned.append(heightmap[self.y - 1][self.x])
        if down:
            objects_returned.append(heightmap[self.y + 1][self.x])
        if right:
            objects_returned.append(heightmap[self.y][self.x + 1])
        if left:
            objects_returned.append(heightmap[self.y][self.x - 1])
        self.walkable_neighbours = objects_returned
        return objects_returned

    def __str__(self):
            return f"({self.height},{self.weight})"

    def __repr__(self):
        return f"{self.weight}"


# Werkt niet ivm memory. Vervangen met een while loop.
def walk_the_walk(startpunt):
    available_paths = startpunt.available_paths()
    walkable_neighbours = startpunt.get_walkable_neighbours(available_paths)
    new_list = walkable_neighbours[:]
    for neighbour in walkable_neighbours:
        startpunt.overwrite_weight(neighbour)
    for neighbour2 in new_list:
        walk_the_walk(neighbour2)

line_heightmap_number = []
heightmap_numbers = []
startpunten = []
for i, line in enumerate(lines):
    line_heightmap_number = []
    for j, char in enumerate(line):
        if char == 'a':
            startpunt_x, startpunt_y = j, i
        if char == 'S':
            char = 'a'
            startpunt_x, startpunt_y = j, i
        if char == "E":
            char = 'z'
            eindpunt_x, eindpunt_y = j, i
        if char == 'a':
            startpunten.append((startpunt_x, startpunt_y))
        line_heightmap_number.append(Point(j, i, height=ord(char)-96))
    heightmap_numbers.append(line_heightmap_number)


heightmap = np.asarray(heightmap_numbers)
heightmap_backup = heightmap[:]
fewest_steps = math.inf

for startpunt_x, startpunt_y in startpunten:
    heightmap = heightmap_backup[:]
    eindpunt = heightmap[eindpunt_y][eindpunt_x]
    startpunt = heightmap[startpunt_y][startpunt_x]
    startpunt.weight = 0
    unvisisted_queue = set()
    unvisisted_queue.add(startpunt)

    while len(unvisisted_queue):
        # print(unvisisted_queue)
        next_visit = unvisisted_queue.pop()
        # print(next_visit)
        neighbours = next_visit.get_walkable_neighbours(next_visit.available_paths())
        # print(f"Neighbours: {neighbours}")
        for neighbour in neighbours:
            next_visit.overwrite_weight(neighbour)
            unvisisted_queue.add(neighbour)

    print(startpunt)
    print(eindpunt.weight)
    if eindpunt.weight < fewest_steps:
        fewest_steps = eindpunt.weight
print(fewest_steps)
