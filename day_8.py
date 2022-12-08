import numpy as np
with open("inputs/input_day8_0.txt", 'r') as f:
    lines = f.readlines()
lines_breakless = []
for line in lines:
    line_without_linebreak = line.strip()
    lines_breakless.append(line_without_linebreak)

lines = lines_breakless
test_input=["30373",
"25512",
"65332",
"33549",
"35390"]

# lines = test_input

horizontal_length = len(lines[0])
vertical_length = len(lines)
forest = np.zeros(( vertical_length, horizontal_length))

for x in range(horizontal_length):
    for y in range(vertical_length):
        forest[y,x] = lines[y][x]
zichtbaar = []
for x in range(1, vertical_length-1):
    for y in range(1, horizontal_length-1):
        links = max(forest[x, :y])
        rechts = max(forest[x, y+1:])
        boven = max(forest[:x, y])
        onder = max(forest[x+1:, y])
        boom = forest[x, y]
        if any (boom > [links, rechts, boven, onder]):
            zichtbaar.append([x,y])

print(zichtbaar)
print(len(zichtbaar)+2*horizontal_length + 2*vertical_length -4)
hoogste_score = 0
for x in range(1, vertical_length-1):
    for y in range(1, horizontal_length-1):
        links = max(forest[x, :y])
        rechts = max(forest[x, y+1:])
        boven = max(forest[:x, y])
        onder = max(forest[x+1:, y])
        boom = forest[x,y]
        if boom > links:
            score_links = y
        else:
            for i, tree_check_blocking_view in enumerate(reversed(forest[x, :y])):
                if boom <= tree_check_blocking_view:
                    score_links = i+1
                    break
        if boom > rechts:
            score_rechts = horizontal_length - y -1
        else:
            for i, tree_check_blocking_view in enumerate(forest[x, y+1:]):
                if boom <= tree_check_blocking_view:
                    score_rechts = i+1
                    break
        if boom > boven:
            score_boven = x
        else:
            for i, tree_check_blocking_view in enumerate(reversed(forest[:x, y])):
                if boom <= tree_check_blocking_view:
                    score_boven = i+1
                    break
        if boom > onder:
            score_onder = vertical_length - x - 1
        else:
            for i, tree_check_blocking_view in enumerate(forest[x+1:, y]):
                if boom <= tree_check_blocking_view:
                    score_onder = i+1
                    break
        score = score_links * score_rechts * score_boven * score_onder
        print(x, y, boom)
        print(score, score_links, score_rechts, score_boven, score_onder)
        if score > hoogste_score:
            hoogste_score = score

print(hoogste_score)
