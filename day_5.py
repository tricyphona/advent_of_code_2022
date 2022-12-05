with open("inputs/input_day5_0.txt", 'r') as f:
    lines = f.readlines()

stacked_crates = lines[0:8]
# stacked_crates = ["    [D]    ",
# "[N] [C]",
# "[Z] [M] [P]"]

stacked_crates_clean = []

# 7 of 2 --> height of initial stack items.
for i in range(7, -1, -1):
    stacked_crates_clean.append(stacked_crates[i][1::4])
stripped_crates_list = [[] for i in range(9)]

for line_of_crates in stacked_crates_clean:
    for i, item_in_row in enumerate(line_of_crates):
        if item_in_row != ' ':
            stripped_crates_list[i].append(item_in_row)
crates_list = stripped_crates_list
print(crates_list)


def get_objects_to_move(crate_row, amount):
    crates = crate_row[-amount:]
    # For exercise 1: uncomment, for exercise 2: comment.
    # crates.reverse()
    return crates


crate_operations = lines[10:]
# crate_operations = ["move 1 from 2 to 1",
#                     "move 3 from 1 to 3",
#                     "move 2 from 2 to 1",
#                     "move 1 from 1 to 2"]
for operation in crate_operations:
    amount_crates_moved, crate_stack_from, crate_stack_destination = map(int, operation.split()[1::2])
    crate_stack_from -= 1  # index in problem start at 1, conversion to python's index.
    crate_stack_destination -= 1  # index in problem start at 1, conversion to python's index.
    crates_to_move = get_objects_to_move(crates_list[crate_stack_from], amount_crates_moved)
    crates_list[crate_stack_from] = crates_list[crate_stack_from][:-amount_crates_moved]
    crates_list[crate_stack_destination].extend(crates_to_move)
print(crates_list)
for crate_stack in crates_list:
    print(crate_stack[-1])
