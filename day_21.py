with open("inputs/input_day21_0.txt", 'r') as f:
    lines = f.readlines()

test_lines = [
    "root: pppw + sjmn",
    "dbpl: 5",
    "cczh: sllz + lgvd",
    "zczc: 2",
    "ptdq: humn - dvpt",
    "dvpt: 3",
    "lfqf: 4",
    "humn: 5",
    "ljgn: 2",
    "sjmn: drzm * dbpl",
    "sllz: 4",
    "pppw: cczh / lfqf",
    "lgvd: ljgn * ptdq",
    "drzm: hmdt - zczc",
    "hmdt: 32"
]

# lines = test_lines


class Monkey:
    def __init__(self, name, number=None, operator=None, monkeys_to_compute=None, waiting=False):
        self.name = name
        self.number = number
        self.waiting = waiting
        self.operator = operator
        self.monkeys_to_compute = monkeys_to_compute

    def __repr__(self):
        return f"{self.name}"

    def compute_monkey(self):
        if self.operator == '+':
            return self.get_number(self.monkeys_to_compute[0]) + self.get_number(self.monkeys_to_compute[1])
        if self.operator == '-':
            return self.get_number(self.monkeys_to_compute[0]) - self.get_number(self.monkeys_to_compute[1])
        if self.operator == '*':
            return self.get_number(self.monkeys_to_compute[0]) * self.get_number(self.monkeys_to_compute[1])
        if self.operator == '/':
            return self.get_number(self.monkeys_to_compute[0]) / self.get_number(self.monkeys_to_compute[1])

    @staticmethod
    def get_number(monkey_name):
        for monkey_to_find in monkeys:
            if monkey_to_find.name == monkey_name and monkey_to_find.number is not None:
                return monkey_to_find.number
            elif monkey_to_find.name == monkey_name:
                return monkey_to_find.compute_monkey()

    def is_equal(self):
        answer_0 = self.get_number(self.monkeys_to_compute[0])
        answer_1 = self.get_number(self.monkeys_to_compute[1])
        return answer_0, answer_1
print(lines)
monkeys = []
for line in lines:
    monkey_line = line.strip().split()[:]
    name = monkey_line[0][0:4]
    if len(monkey_line) <= 2:
        number = int(monkey_line[1])
        monkeys.append(Monkey(name, number=number))
    else:
        result_math_monkeys = monkey_line[-3::2]
        operator = monkey_line[-2]
        waiting = True
        monkeys.append(Monkey(name, operator=operator, monkeys_to_compute=result_math_monkeys, waiting=True ))


for root in monkeys:
    if root.name == 'root':
        start_monkey = root

print(f"Uitkomst van monkey root is: {start_monkey.compute_monkey()}")

# part 2

for my_monkey in monkeys:
    if my_monkey.name == 'humn':
        break

j = 0
base_number = 1
base_number_found = False
while not base_number_found:
    my_monkey.number = base_number
    answer_0, answer_1 = start_monkey.is_equal()
    if answer_0 > answer_1:
        base_number *= 10
    else:
        base_number_found = True

found_numbers = 0
while base_number > 0.1:
    i = j * base_number + found_numbers
    my_monkey.number = i
    answer_0, answer_1 = start_monkey.is_equal()
    if (answer_0 - answer_1) < 0:
        found_numbers += (j -1) * base_number
        j = 0
        base_number //= 10
    else:
        j += 1
    if answer_0 == answer_1:
        print(f"Schreeuw {i}!")
