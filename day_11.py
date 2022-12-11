with open("inputs/input_day11_0.txt", 'r') as f:
    lines = f.readlines()

print(lines)

test_case = [
"Monkey 0:",
"Starting items: 79, 98",
"Operation: new = old * 19",
"Test: divisible by 23",
"If true: throw to monkey 2",
"If false: throw to monkey 3",
"\n",
"Monkey 1:",
"Starting items: 54, 65, 75, 74",
"Operation: new = old + 6",
"Test: divisible by 19",
"If true: throw to monkey 2",
"If false: throw to monkey 0",
"\n",
"Monkey 2:",
"Starting items: 79, 60, 97",
"Operation: new = old * old",
"Test: divisible by 13",
"If true: throw to monkey 1",
"If false: throw to monkey 3",
"\n",
"Monkey 3:",
"Starting items: 74",
"Operation: new = old + 3",
"Test: divisible by 17",
"If true: throw to monkey 0",
"If false: throw to monkey 1"]

# lines = test_case
rounds_of_shenanigans = 20

class Monkey:
    total_amount_monkeys = 0
    total_test_value = 1  # combinatie testvalue Monkeys → je kan de combinatie van test values veilig van worry afhalen
    # zonder dat dit effect heeft op de test case voor iedere Monkey.
    part = 1

    def __init__(self, id, starting_items, operator, operator_value, test_value,action_if_test_true, action_if_test_false):
        Monkey.total_amount_monkeys += 1
        self.id = id
        if starting_items is None:
            self.items = []
        else:
            self.items = starting_items
        self.operator = operator
        self.operator_value = operator_value
        self.test_value = test_value
        self.action_if_test_true = action_if_test_true
        self.action_if_test_false = action_if_test_false
        self.new_items = []
        self.inspected_items = 0
        Monkey.total_test_value *= self.test_value

    def inspect_item(self, item):
        if self.operator_value == 'old':
            worry_level = item**2
        else:
            worry_level = eval(f"{item} {self.operator} {self.operator_value}")

        if Monkey.part == 1:
            worry_level_bored = worry_level // 3
        elif Monkey.part == 2:
            worry_level_bored = worry_level % Monkey.total_test_value
        self.inspected_items += 1
        item = worry_level_bored
        if not worry_level_bored % self.test_value:
            self.throw_item_to_monkey(self.action_if_test_true, item)
        else:
            self.throw_item_to_monkey(self.action_if_test_false, item)

    def throw_item_to_monkey(self, monkey, item):
        all_monkeys[monkey].items.append(item)
        #print(f"Monkey: {self.id} throws to {monkey} item: {item}")

    def __eq__(self, other):
        return self.inspected_items == other.inspected_items

    def __lt__(self, other):
        return self.inspected_items < other.inspected_items

    def __gt__(self, other):
        return self.inspected_items > other.inspected_items

    def __ge__(self, other):
        return self.inspected_items >= other.inspected_items

    def __le__(self, other):
        return self.inspected_items <= other.inspected_items



def get_input(lines, all_monkeys):
    for line in lines:
        if line == '\n':
            continue
        line = line.split()
        first_command, second_list = line[0], line[1:]
        if first_command == 'Monkey':
            monkey_id = second_list[0].split(':')[0]
            monkey_id = int(monkey_id)
        if first_command == 'Starting':
            items = []
            for item in second_list[1:]:
                items.append(item.strip(','))
            items = list(map(int, items))
        if first_command == 'Operation:':
            operator = second_list[-2]
            operator_value = second_list[-1]
        if first_command == 'Test:':
            test_value = int(second_list[-1])
        if first_command == 'If':
            if second_list[0] == 'true:':
                to_monkey_true = int(second_list[-1])
            elif second_list[0] == 'false:':
                to_monkey_false = int(second_list[-1])
                all_monkeys.append(
                    Monkey(monkey_id, items, operator, operator_value, test_value, to_monkey_true, to_monkey_false))


def print_items(all_monkeys):
    for i in range(len(all_monkeys)):
        print(f"Monkey {i}'s items: {all_monkeys[i].items}")
    print('')


def monkey_shenanigans(rounds_of_shenanigans, all_monkeys):
    for i in range(rounds_of_shenanigans):
        for monkey in all_monkeys:
            for j in range(len(monkey.items)):
                item = monkey.items.pop(0)
                monkey.inspect_item(item)

def print_number_of_inspected_items(all_monkeys):
    for i in range(len(all_monkeys)):
        print(f"Monkey {i} has {all_monkeys[i].inspected_items} times inspected an item.")
    print()

all_monkeys = []
get_input(lines, all_monkeys)
#part 1:

print_items(all_monkeys)
monkey_shenanigans(rounds_of_shenanigans, all_monkeys)
print_items(all_monkeys)
print_number_of_inspected_items(all_monkeys)
active_monkeys = sorted(all_monkeys, reverse=True)
print(f"Level of monkey business: "
      f"{active_monkeys[0].inspected_items} * {active_monkeys[1].inspected_items} = "
      f"{active_monkeys[0].inspected_items * active_monkeys[1].inspected_items}")

print('\n\n')
print("Part 2:")
all_monkeys = []
get_input(lines, all_monkeys)
Monkey.part = 2
rounds_of_shenanigans = 10000

print_items(all_monkeys)
monkey_shenanigans(rounds_of_shenanigans, all_monkeys)
print_items(all_monkeys)
print_number_of_inspected_items(all_monkeys)
active_monkeys = sorted(all_monkeys, reverse=True)
print(f"Level of monkey business: "
      f"{active_monkeys[0].inspected_items} * {active_monkeys[1].inspected_items} = "
      f"{active_monkeys[0].inspected_items * active_monkeys[1].inspected_items}")