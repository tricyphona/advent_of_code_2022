with open("inputs/input_day20_0.txt", 'r') as f:
    lines = f.readlines()

test_input = [
    "1",
    "2",
    "-3",
    "3",
    "-2",
    "0",
    "4"
]


class Item:
    def __init__(self, value):
        self.value = int(value) * 811589153
        self.moved = False
        self.order = None
    def __repr__(self):
        return f"{self.value}"


# lines = test_input
lines2 = []
for line in lines:
    line = line.strip()
    lines2.append(Item(int(line)))


i = len(lines2)
items_visited = 0
for k in range(1):
    print(lines2)
    items_visited = 0
    print(k)
    for item in lines2:
        item.moved = False
    while items_visited < i:
        for j in range(i):
            if lines2[j].moved:
                continue
            else:
                value = lines2.pop(j)
                if value.value == 0:
                    lines2.insert(j, value)
                else:
                    new_position = j + value.value
                    while new_position < 0:
                        new_position %= i-1
                        new_position += i
                        new_position -= 1
                    while new_position > i:
                        new_position %= i-1
                    if new_position % i:
                        lines2.insert(new_position, value)
                    else:
                        lines2.append(value)
                value.moved = True
                value.order = items_visited
                items_visited += 1
                last_line = lines2[:]
                break

print(lines2)

for z in range(2,11):
    item_index = 0
    items_visited = 0
    while items_visited < i:
        for j in range(i):
            if lines2[j].order == item_index:
                value = lines2.pop(j)
                if value.value == 0:
                    lines2.insert(j, value)
                else:
                    new_position = j + value.value
                    while new_position < 0:
                        new_position %= i - 1
                        if new_position != 1:
                            new_position += i
                            new_position -= 1
                    while new_position > i:
                        new_position %= i - 1
                    if new_position % i:
                        lines2.insert(new_position, value)
                    else:
                        lines2.append(value)
                items_visited += 1
                last_line = lines2[:]
                item_index += 1
                break
    print(z, lines2)

lines3 = []
for i in lines2:
    lines3.append(i.value)

print(lines3.index(0))
print(lines3[(lines3.index(0)+1000)%len(lines3)])
print(lines3[(lines3.index(0)+2000)%len(lines3)])
print(lines3[(lines3.index(0)+3000)%len(lines3)])
answer = (lines3[(lines3.index(0)+1000)%len(lines3)]) + (lines3[(lines3.index(0)+2000)%len(lines3)]) + (lines3[(lines3.index(0)+3000)%len(lines3)])
print(answer)
