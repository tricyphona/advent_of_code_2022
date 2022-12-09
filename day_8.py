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

def vind_hoogsteboom_vanuit_xy_gezien(forest, x, y):
    hoogsteboom_links = max(forest[x, :y])
    hoogsteboom_rechts = max(forest[x, y + 1:])
    hoogsteboom_boven = max(forest[:x, y])
    hoogsteboom_onder = max(forest[x + 1:, y])
    return hoogsteboom_links, hoogsteboom_rechts, hoogsteboom_boven, hoogsteboom_onder


horizontal_length = len(lines[0])
vertical_length = len(lines)
forest = np.zeros(( vertical_length, horizontal_length))

for x in range(horizontal_length):
    for y in range(vertical_length):
        forest[y,x] = lines[y][x]
zichtbare_bomen = []
for x in range(1, vertical_length-1):
    for y in range(1, horizontal_length-1):
        hoogsteboom_links, hoogsteboom_rechts, hoogsteboom_boven, hoogsteboom_onder = \
            vind_hoogsteboom_vanuit_xy_gezien(forest, x, y)
        boom = forest[x, y]
        if any(boom > [hoogsteboom_links, hoogsteboom_rechts, hoogsteboom_boven, hoogsteboom_onder]):
            zichtbare_bomen.append([x, y])

print(zichtbare_bomen)
print(len(zichtbare_bomen) + 2 * horizontal_length + 2 * vertical_length - 4)
hoogste_score = 0
# Voor alle bomen die niet aan de rand staan:
for x in range(1, vertical_length-1):
    for y in range(1, horizontal_length-1):
        hoogsteboom_links = max(forest[x, :y])
        hoogsteboom_rechts = max(forest[x, y + 1:])
        hoogsteboom_boven = max(forest[:x, y])
        hoogsteboom_onder = max(forest[x + 1:, y])
        boom = forest[x,y]
        if boom > hoogsteboom_links:
            score_links = y
        else:
            for i, tree_check_blocking_view in enumerate(reversed(forest[x, :y])):
                if boom <= tree_check_blocking_view:
                    score_links = i+1
                    break
        if boom > hoogsteboom_rechts:
            score_rechts = horizontal_length - y - 1
        else:
            for i, tree_check_blocking_view in enumerate(forest[x, y+1:]):
                if boom <= tree_check_blocking_view:
                    score_rechts = i+1
                    break
        if boom > hoogsteboom_boven:
            score_boven = x
        else:
            for i, tree_check_blocking_view in enumerate(reversed(forest[:x, y])):
                if boom <= tree_check_blocking_view:
                    score_boven = i+1
                    break
        if boom > hoogsteboom_onder:
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
