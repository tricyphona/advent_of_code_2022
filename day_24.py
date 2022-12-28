import numpy as np
with open("inputs/input_day24_0.txt", 'r') as f:
    lines = f.readlines()

test_lines = [
    "#E######",
    "#>>.<^<#",
    "#.<..<<#",
    "#>v.><>#",
    "#<^v^^>#",
    "######.#"
]

test_lines2 = [
"#.#####",
"#.....#",
"#>....#",
"#.....#",
"#...v.#",
"#.....#",
"#####.#"
]
# lines = test_lines
print(lines)
height = len(lines)
width = len(lines[0].strip())
print(height, width)
board = np.zeros((height,width), int)

class Storm:
    def __init__(self, x, y, char):
        self.x_origin = x
        self.y_origin = y
        self.x = x
        self.y = y
        self.direction_x, self.direction_y = self.get_direction(char)
        self.char = char

    @staticmethod
    def get_direction(char):
        if char == '>':
            return 1, 0
        if char == '<':
            return -1, 0
        if char == '^':
            return 0, -1
        if char == 'v':
            return 0, 1

    def move_storm(self):
        if self.direction_x != 0:
            if (0 >= (self.x + self.direction_x)) or ((self.x + self.direction_x) >= (width-1)):
                if self.direction_x > 0:
                    self.x = 1
                else:
                    self.x = width-2
            else:
                self.x += self.direction_x

        if self.direction_y != 0:
            if (0 >= (self.y + self.direction_y)) or ((self.y + self.direction_y) >= (height-1)):
                if self.direction_y > 0:
                    self.y = 1
                else:
                    self.y = height-2
            else:
                self.y += self.direction_y

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.direction_x, self.direction_y}, {self.char})"

class Human:
    def __init__(self, x=1, y=0):
        self.x = x
        self.y = y

    def move(self):
        options = []
        available_stay, available_right, available_left, available_up, available_down = True, True, True, True, True
        for storm in storms:
            if (self.x, self.y) == (storm.x, storm.y):
                available_stay = False
            if (self.x+1, self.y) == (storm.x, storm.y) or self.x+1 >= width-1 or self.y <= 0 or self.y >= height-1:
                available_right = False
            if (self.x-1, self.y) == (storm.x, storm.y) or self.x - 1 <= 0 or self.y <= 0 or self.y >= height-1:
                available_left = False
            if (self.x, self.y-1) == (storm.x, storm.y) or self.y - 1 <= 0:
                available_up = False
            if (self.x, self.y+1) == (storm.x, storm.y) or self.y + 1 >= height - 1:
                available_down = False
            # f"{(self.x, self.y) == (storm.x, storm.y) or board[self.y][self.x] == 1},{(self.x+1, self.y) == (storm.x, storm.y) or board[self.y][self.x+1] == 1},{(self.x-1, self.y) == (storm.x, storm.y) or board[self.y][self.x-1] == 1},{(self.x, self.y-1) == (storm.x, storm.y) or board[self.y-1][self.x] == 1},{(self.x, self.y+1) == (storm.x, storm.y) or board[self.y+1][self.x] == 1}"
            # print(available_stay, available_right, available_left, available_up, available_down)
        if available_stay:
            options.append((self.x, self.y))
        if available_right:
            options.append((self.x + 1, self.y))
        if available_left:
            options.append((self.x - 1, self.y))
        if available_up:
            options.append((self.x, self.y - 1))
        if available_down:
            options.append((self.x, self.y + 1))
        # print(options)
        return options

    def __repr__(self):
        return f"Human: {self.x, self.y}"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

storms = set()
for y, line in enumerate(lines):
    line = line.strip()
    for x, char in enumerate(line):
        if char in ['<', '>', '^', 'v']:
            storms.add(Storm(x,y, char))
            # print(Storm(x,y, char))
        elif char == '#':
            board[y][x] = 1

board[0][1] = 1
board[height-1][width-1] = 1
print(board)
# print(storms)
# for storm in storms:
#     storm.move_storm()

# print(Human().move())
human = Human()
step = 0
solution = []
found_path = False
humans = set()
humans.add(human)
humans_new = set()

def get_path(humans, destination_x, destination_y, step):
    humans_new = set()
    while True:
        # board2 = board.copy()
        step += 1
        print(step)
        for storm in storms:
            storm.move_storm()

        # print(len(humans))
        for human in humans:
            # print(human)
            if (human.x, human.y) == (destination_x, destination_y):
                return step
            opties = human.move()
            for optie in opties:
                humans_new.add(Human(optie[0], optie[1]))
        humans = humans_new
        humans_new = set()
        # for storm in storms:
        #     board2[storm.y][storm.x] += 3
        # for human in humans:
        #     board2[human.y][human.x] += 8
        # print(board2)
        pass

step = get_path(humans, width-2,height-2,step)
# input()
start_location_x = width - 2
start_location_y = height - 1
human = Human(start_location_x, start_location_y)
humans = set()
humans.add(human)
destination_x = 1
destination_y = 1
step = get_path(humans, destination_x, destination_y, step)
print(step)
# input()
destination_x = width - 2
destination_y = height - 2
humans = set()
human = Human(1, 0)
humans.add(human)
step = get_path(humans, destination_x, destination_y,step)
# print(step)


