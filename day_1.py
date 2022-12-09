with open("inputs/input_day1_0.txt", 'r') as f:
    lines = f.readlines()

new_lines = [x.replace('\n', '') for x in lines]


class Elf:
    elf_counter = 0

    def __init__(self):
        self.calories_carried = 0
        self.elf_counter = Elf.elf_counter
        Elf.elf_counter += 1

    def __int__(self):
        return self.calories_carried

    def __repr__(self):
        return f"{self.elf_counter}: {self.calories_carried}"

    def __eq__(self, other):
        return self.calories_carried == other.calories_carried

    def __lt__(self, other):
        return self.calories_carried < other.calories_carried

    def __gt__(self, other):
        return self.calories_carried > other.calories_carried

    def __ge__(self, other):
        return self.calories_carried >= other.calories_carried

    def __le__(self, other):
        return self.calories_carried <= other.calories_carried

    def __add__(self, other):
        return self.calories_carried + other.calories_carried

    def __radd__(self, other):
        return other + self.calories_carried


all_elves = [Elf()]
for calorie_value in new_lines:
    if calorie_value == '':
        all_elves.append(Elf())
    else:
        all_elves[-1].calories_carried += int(calorie_value)

print(max(all_elves))
all_elves.sort(reverse=True)
print(all_elves)
print(sum(all_elves[0:3]))
