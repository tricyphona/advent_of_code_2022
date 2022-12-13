import ast
import functools

with open("inputs/input_day13_0.txt", 'r') as f:
    lines = f.readlines()

test_input = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]"
]


def create_pairs(input_day13):
    pair = []
    pairs = []
    for line in input_day13:
        line = line.strip()
        if line != '':
            line_input = ast.literal_eval(line)
            pair.append(line_input)
        else:
            pairs.append(pair)
            pair = []
    pairs.append(pair)
    return pairs


class Signal:
    @staticmethod
    def check_if_item_eq_list(object_input):
        return isinstance(object_input, list)

    @staticmethod
    def compare_ints(self_int, other_int):
        if self_int < other_int:
            return 1
        if self_int > other_int:
            return 0
        if self_int == other_int:
            return 2

    @staticmethod
    def convert_to_list(integer):
        return [integer]

    @staticmethod
    def compare_lists(self_list, other_list):
        for self_item, other_item in zip(self_list, other_list):
            if not Signal.check_if_item_eq_list(self_item) and not Signal.check_if_item_eq_list(other_item):
                outcome = Signal.compare_ints(self_item, other_item)
                if outcome == 1:
                    return True
                elif outcome == 0:
                    return False
                elif outcome == 2:
                    pass
            elif Signal.check_if_item_eq_list(self_item) and Signal.check_if_item_eq_list(other_item):
                outcome = Signal.compare_lists(self_item, other_item)
                if outcome is True:
                    return True
                elif outcome is False:
                    return False
                else:
                    pass
            elif not Signal.check_if_item_eq_list(self_item) and Signal.check_if_item_eq_list(other_item):
                self_item_list = Signal.convert_to_list(self_item)
                outcome = Signal.compare_lists(self_item_list, other_item)
                if outcome is True:
                    return True
                elif outcome is False:
                    return False
                else:
                    pass
            elif Signal.check_if_item_eq_list(self_item) and not Signal.check_if_item_eq_list(other_item):
                other_item_list = Signal.convert_to_list(other_item)
                outcome = Signal.compare_lists(self_item, other_item_list)
                if outcome is True:
                    return True
                elif outcome is False:
                    return False
                else:
                    pass
        if len(self_list) < len(other_list):
            return True
        elif len(self_list) > len(other_list):
            return False
        else:
            pass


def compare_signal(item1, item2):
    outcome = Signal.compare_lists(item1, item2)
    if outcome is True:
        return -1
    else:
        return 1

# lines = test_input

pairs = create_pairs(lines)
sum_right_indices = 0
for i, pair in enumerate(pairs):
    if Signal.compare_lists(pair[0], pair[1]):
        sum_right_indices += i+1
print(sum_right_indices)

# Part 2
part2_list = []
for pair in pairs:
    part2_list.append(pair[0])
    part2_list.append(pair[1])
part2_list.append([[2]])
part2_list.append([[6]])
print(part2_list)

part2_list.sort(key=functools.cmp_to_key(compare_signal))
print(part2_list)

print(f"positie begin: {part2_list.index([[2]]) + 1}, positie eind: {part2_list.index([[6]]) + 1} \n"
      f"uitkomst: {(part2_list.index([[2]]) + 1) * (part2_list.index([[6]]) + 1)}")