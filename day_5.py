with open("inputs/input_day5_0.txt", 'r') as f:
    lines = f.readlines()

stacked_crates = lines[0:8]
# stacked_crates = ["    [D]    ",
# "[N] [C]",
# "[Z] [M] [P]"]

input_crates_as_str_with_whitespace = []
height_stacked_crates = len(stacked_crates)
for i in range(height_stacked_crates-1, -1, -1):
    input_crates_as_str_with_whitespace.append(stacked_crates[i][1::4])

crates_as_list_per_row = [[] for i in range(9)]
for line_of_crates in input_crates_as_str_with_whitespace:
    for i, item_in_row in enumerate(line_of_crates):
        if item_in_row != ' ':
            crates_as_list_per_row[i].append(item_in_row)
crate_stacks = crates_as_list_per_row
print(crate_stacks)


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
    crates_to_move = get_objects_to_move(crate_stacks[crate_stack_from], amount_crates_moved)
    crate_stacks[crate_stack_from] = crate_stacks[crate_stack_from][:-amount_crates_moved]
    crate_stacks[crate_stack_destination].extend(crates_to_move)
print(crate_stacks)
for crate_stack in crate_stacks:
    print(crate_stack[-1], end='')
