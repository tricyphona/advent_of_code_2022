with open("inputs/input_day4_0.txt", 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

test = ["2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"]
#lines = test


class Elf:
    elf_id = 0

    def __init__(self, clean_range):
        self.lowest = int(clean_range[0])
        self.highest = int(clean_range[-1])
        self.elf_id = Elf.elf_id
        Elf.elf_id += 1

    @staticmethod
    def is_fully_contained(self, other):
        if self.lowest >= other.lowest and self.highest <= other.highest:
            return True
        return False

    @staticmethod
    def overlap(self, other):
        if self.lowest < other.lowest and self.highest < other.lowest:
            return False
        if self.highest > other.lowest and self.highest > other.highest:
            return False
        return True

    def __eq__(self, other):
        return self.lowest == other.lowest and self.highest == other.highest

    def __repr__(self):
        return f"{self.elf_id}: {self.lowest} -- {self.highest}"


all_elves = []
compare_temp_list = [None,None]
fully_contained = 0
for line in lines:
    elves_to_compare = line.split(',')
    for i, elf_to_compare in enumerate(elves_to_compare):
        compare_temp_list[i] = Elf(elf_to_compare.split('-'))
    if compare_temp_list[0] == compare_temp_list[1]:
        fully_contained += 1
    elif Elf.is_fully_contained(compare_temp_list[0],compare_temp_list[1]):
        fully_contained += 1
    elif Elf.is_fully_contained(compare_temp_list[1], compare_temp_list[0]):
        fully_contained += 1

print(fully_contained)

count_overlap = 0
for line in lines:
    elves_to_compare = line.split(',')
    for i, elf_to_compare in enumerate(elves_to_compare):
        compare_temp_list[i] = Elf(elf_to_compare.split('-'))
    if Elf.overlap(compare_temp_list[0],compare_temp_list[1]):
        count_overlap += 1
    elif Elf.overlap(compare_temp_list[1],compare_temp_list[0]):
        count_overlap += 1

print(count_overlap)
