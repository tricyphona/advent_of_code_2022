import numpy as np
with open("inputs/input_day23_0.txt", 'r') as f:
    lines = f.readlines()

height = len(lines)
width = len(lines[0].strip())

field = np.zeros((len(lines)+20, len(lines[0].strip())+20))

for y, line in enumerate(lines):
    y += 10
    line.strip()
    for x, char in enumerate(line):
        x += 10
        if char == '#':
            field[y][x] = 1

