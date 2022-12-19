import numpy as np
with open("inputs/input_day17_0.txt", 'r') as f:
    lines = f.read().strip()
# lines = open('inputs/input_day17_0.txt', 'r').read().strip()
vertical_size = 5000
tetris_board = np.zeros((vertical_size, 7), dtype=np.int8)
print(lines)
print(len(lines))
test_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
# lines = test_input

for row in tetris_board:
    if all (row > 0):
        print("TODO, remove line & under")

def test_if_object_is_free(shape, y,x):
    if shape == "h_line":
        if 0 > x or x >= 4:
            return False
        return all(tetris_board[y, x:x+4] == 0)
    if shape == "cross":
        if 0 > x or x >= 5:
            return False
        return tetris_board[y, x+1] == 0 and all(tetris_board[y+1, x:x+3] == 0) and tetris_board[y+2, x+1] == 0
    if shape == "corner":
        if 0 > x or x >= 5:
            return False
        return all(tetris_board[y:y+3, x+2] == 0) and all(tetris_board[y+2, x:x+3] == 0)
    if shape == "v_line":
        if 0 > x or x >= 7:
            return False
        return all(tetris_board[y:y+4, x] == 0)
    if shape == "box":
        if 0 > x or x >= 6:
            return False
        return all(tetris_board[y:y+2, x] == 0) and all(tetris_board[y:y+2, x+1] == 0)

def pushed(shape, y,x,wind):
    if wind == ">" and test_if_object_is_free(shape, y, x+1):
        return y, x+1
    elif wind == "<" and test_if_object_is_free(shape, y, x-1):
        return y, x-1
    else:
        return y, x

def fall_down(shape, y, x):
    if test_if_object_is_free(shape, y+1, x):
        return True
    else:
        draw_object(shape, y, x)
        return False

def draw_object(shape, y, x):
    if shape == "h_line":
        tetris_board[y, x:x + 4] = 1
    elif shape == "cross":
        tetris_board[y, x+1] = 1
        tetris_board[y + 1, x:x + 3] = 1
        tetris_board[y + 2, x+1] = 1
    elif shape == "corner":
        tetris_board[y:y + 3, x + 2] = 1
        tetris_board[y+2, x:x + 3] = 1
    elif shape == "v_line":
        tetris_board[y:y+4, x] = 1
    elif shape == "box":
        tetris_board[y:y+2, x:x+2] = 1

def spawn_object(shape, y=vertical_size-1):
    if shape == "h_line":
        x = 2
    elif shape == "cross":
        x = 2
        y -= 2
    elif shape == "corner":
        x=2
        y -= 2
    elif shape == "v_line":
        x = 2
        y -= 3
    elif shape == "box":
        x = 2
        y -= 1
    y -= 4
    return int(y), int(x)

print()
# draw_object("h_line", 0, 0)


top_line = 0

shapes = ["h_line", "cross", "corner", "v_line", "box"]
y = 0
if y == 0 and not test_if_object_is_free("v_line",y,0):
    print("Oh no")

i=0
k = 0
y, x = spawn_object(shapes[k])
print(shapes[k])
j = 0
tetris_board[vertical_size-1, :] = 1
objecten = 1
min_y = vertical_size
while objecten < 2023:
    i = i % len(lines)
    wind = lines[i]
    i += 1
    y, x = pushed(shapes[k], y, x, wind)
    if fall_down(shapes[k], y, x):
        y += 1
    else:
        y_old = y
        if y < min_y:
            min_y = y
        old_shape = shapes[k]
        k += 1
        k = k % len(shapes)
        y,x = spawn_object(shapes[k], min_y)
        # if k == 3:
        #     draw_object(shapes[k], y, x)
        objecten += 1


print(tetris_board[vertical_size-50:vertical_size,:])
print(vertical_size-y_old-1)