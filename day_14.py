import numpy as np
with open("inputs/input_day14_0.txt", 'r') as f:
    lines = f.readlines()

test_lines = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]
# lines = test_lines
# print(lines)
cave = []
max_x, max_y = 0,0
min_x, min_y = 10000,0
for line in lines:
    points = line.split()[0::2]
    rocks = []
    for point in points:
        point_x, point_y = map(int, point.split(','))
        if point_x > max_x:
            max_x = point_x
        if point_y > max_y:
            max_y = point_y
        if point_x < min_x:
            min_x = point_x
        if point_y < min_y:
            min_y = point_y
        rocks.append([int(point_x), int(point_y)])
    cave.append(rocks)

# print(cave)
print(max_x, max_y)
print(min_x, min_y)
min_x -= 200
max_x += 200
min_y = 0
max_y += 2
numpy_cave = np.zeros((max_y+1-min_y, max_x+1-min_x))
numpy_cave[max_y][:] = 1
print(numpy_cave)
print(numpy_cave.shape)

def create_rocks(cave, numpy_cave):
    for line in cave:
        print(line)
        for index_corner in range(len(line)-1):
            rock_row_x = line[index_corner+1][0] - line[index_corner][0]
            rock_row_y = line[index_corner + 1][1] - line[index_corner][1]
            print(rock_row_x)
            print(rock_row_y)
            if rock_row_x == 0 and rock_row_y == 1 and line[index_corner][0] == 581:
                pass
            start_x = line[index_corner][0]
            start_y = line[index_corner][1]
            if rock_row_x:
                y = start_y - min_y
                if rock_row_x > 0:
                    direction = 1
                    rock_row_x += 1
                else:
                    direction = -1
                    rock_row_x -= 1
                for x in range(start_x, start_x + rock_row_x, direction):
                    x -= min_x
                    numpy_cave[y][x] = 1
                    print(x, y)
            elif rock_row_y:
                x = start_x - min_x
                if rock_row_y > 0:
                    direction = 1
                    rock_row_y += 1
                else:
                    direction = -1
                    rock_row_y -= 1
                for y in range(start_y, start_y + rock_row_y, direction):
                    y -= min_y
                    numpy_cave[y][x] = 1
                    print(x, y)

create_rocks(cave, numpy_cave)
print(numpy_cave)
print(numpy_cave.shape)


class Sand:
    def __init__(self, min_x):
        self.position_x = 500 - min_x
        self.position_y = 0

    def fall_down(self):
        if numpy_cave[self.position_y + 1][self.position_x] == 0:
            self.position_y += 1
            return True
        elif numpy_cave[self.position_y + 1][self.position_x - 1] == 0:
            self.position_y += 1
            self.position_x -= 1
            return True
        elif numpy_cave[self.position_y + 1][self.position_x + 1] == 0:
            self.position_y += 1
            self.position_x += 1
            return True
        else:
            numpy_cave[self.position_y][self.position_x] = 2
            if self.position_y == 0:
                return False
            else:
                return False

first_sand = Sand(min_x)
while first_sand.fall_down():
    pass

print(numpy_cave)
sand = []
i = 0
while True:
    i += 1
    sand.append(Sand(min_x))
    try:
        while sand[-1].fall_down():
            pass
    except IndexError as e:
        print(i)
        break
    if sand[-1].position_y == 0:
        print(i+1)
        print("alles is vol!")
        break

print(numpy_cave)