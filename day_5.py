with open("inputs/input_day5_0.txt", 'r') as f:
    lines = f.readlines()

stacked_crates = lines[0:8]
# stacked_crates = ["    [D]    ",
# "[N] [C]",
# "[Z] [M] [P]"]

stacked_crates_clean = []

#7 of 2 --> hight of initial stack items.
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
    #crates.reverse()
    return crates

crate_operations = lines[10:]
# crate_operations = ["move 1 from 2 to 1",
#                     "move 3 from 1 to 3",
#                     "move 2 from 2 to 1",
#                     "move 1 from 1 to 2"]
for operation in crate_operations:
    move_operation, from_operation, to_operation = map(int, operation.split()[1::2])
    from_operation -= 1 #index in problem start at 1, conversion to python's index.
    to_operation -= 1 #index in problem start at 1, conversion to python's index.
    objects_to_move = get_objects_to_move(crates_list[from_operation], move_operation)
    crates_list[from_operation] = crates_list[from_operation][:-move_operation]
    crates_list[to_operation].extend(objects_to_move)
print(crates_list)
for crate_stack in crates_list:
    print(crate_stack[-1])
