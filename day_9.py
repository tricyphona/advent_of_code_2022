with open("inputs/input_day9_0.txt", 'r') as f:
    lines = f.readlines()
lines_no_breaks = []
for line in lines:
    line_without_linebreak = line.strip()
    lines_no_breaks.append(line_without_linebreak)

test_case1 = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"
     ]

test_case2 = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20"
    ]
# lines_no_breaks = test_case1
# lines_no_breaks = test_case2


class Rope:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = set()
        self.visited.add(self.get_location())

    def get_location(self):
        return self.x, self.y

    def catch_up(self, move_x=0, move_y=0):
        self.x += move_x
        self.y += move_y
        self.visited.add(self.get_location())

    def check_distance_too_big(self, other):
        return self.x + 1 < other.x or self.x - 1 > other.x or self.y + 1 < other.y or self.y - 1 > other.y

    def get_movement(self, other):
        if self.x < other.x:
            move_x = 1
        elif self.x > other.x:
            move_x = -1
        else:
            move_x = 0

        if self.y < other.y:
            move_y = 1
        elif self.y > other.y:
            move_y = -1
        else:
            move_y = 0

        return move_x, move_y


rope_length = 10  # of 2
print(lines_no_breaks)
head = Rope()
tails = [Rope() for i in range(rope_length - 1)]  # head telt als eerste rope
for instruction in lines_no_breaks:
    direction, distance = instruction.split()
    for i in range(int(distance)):
        if direction == 'R':
            head.x += 1
        elif direction == 'L':
            head.x -= 1
        elif direction == 'U':
            head.y += 1
        elif direction == 'D':
            head.y -= 1
        for j in range(len(tails)):
            if j == 0:
                if tails[j].check_distance_too_big(head):
                    move_x, move_y = tails[j].get_movement(head)
                    tails[j].catch_up(move_x, move_y)
            else:
                if tails[j].check_distance_too_big(tails[j - 1]):
                    move_x, move_y = tails[j].get_movement(tails[j - 1])
                    tails[j].catch_up(move_x, move_y)

print(tails[rope_length - 2].visited)
print(len(tails[rope_length - 2].visited))
