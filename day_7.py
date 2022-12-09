with open("inputs/input_day7_0.txt", 'r') as f:
    lines = f.readlines()

# lines = ["$ cd /",
# "$ ls",
# "dir a",
# "14848514 b.txt",
# "8504156 c.dat",
# "dir d",
# "$ cd a",
# "$ ls",
# "dir e",
# "29116 f",
# "2557 g",
# "62596 h.lst",
# "$ cd e",
# "$ ls",
# "584 i",
# "$ cd ..",
# "$ cd ..",
# "$ cd d",
# "$ ls",
# "4060174 j",
# "8033020 d.log",
# "5626152 d.ext",
# "7214296 k"]


class Directory:
    def __init__(self, items=None, parent=None, name="/"):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.name = name
        self.size = 0
        self.parent = parent

    def add_item(self, item_size):
        self.size += int(item_size)
        if self.parent is not None:
            self.parent.add_item(item_size)

    def __repr__(self):
        return f"{self.name}: met grootte {self.size}"

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __le__(self, other):
        return self.size <= other.size

    def __add__(self, other):
        return self.size + other.size

    def __radd__(self, other):
        return other + self.size


directories = []
working_dir = Directory()
for line in lines:
    line = line.split()
    print(line)
    if line[0] == '$' and line[1] == 'cd':
        instruction = line[2:][0]
        print(instruction)
        if instruction == '..':
            working_dir = working_dir.parent
        else:
            new_directory = Directory(parent=working_dir, name=instruction)
            directories.append(new_directory)
            working_dir = new_directory
    elif line == "dir":
        print("dir")
    elif line[0].isdigit():
        working_dir.add_item(line[0])
directories.sort()
sum_dirs = 0

for dir in directories:
    if dir.size <= 100000:
        sum_dirs += dir.size
print(sum_dirs)
size_needed = 30000000
total_disk_space = 70000000
disk_used = max(directories)
disk_used = disk_used.size
space_to_clean = total_disk_space - disk_used - size_needed
space_to_clean *= -1
for dir in directories:
    if dir.size > space_to_clean:
        print(dir)
