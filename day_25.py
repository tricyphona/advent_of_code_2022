with open("inputs/input_day25_0.txt", 'r') as f:
    lines = f.readlines()

test_input = [
    "1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122"
]

# lines = test_input
total_value = 0
# lines = ["2==-==---="]
for line in lines:
    line = line.strip()
    value_line = 0
    for i, value in enumerate(line):
        if value == '1':
            value = 1
        elif value == '2':
            value = 2
        elif value == '0':
            value = 0
        elif value == '=':
            value = -2
        elif value == '-':
            value = -1
        value_line += 5 ** (len(line) - i - 1) * value
    print(value_line)
    total_value += value_line
print(total_value)
val_list = []


def to_snafu(value, add_one=False):
    if add_one:
        value += 1
    if value % 5 == 0 or value % 5 == 5:
        last = "0"
        add_one = False
    if value % 5 == 1 or value % 5 == 6:
        last = "1"
        add_one = False
    if value % 5 == 2 or value % 5 == 7:
        last = "2"
        add_one = False
    if value % 5 == 3 or value % 5 == 8:
        last = "="
        add_one = True
    if value % 5 == 4 or value % 5 == 9:
        last = '-'
        add_one = True
    val_list.append(last)
    if value > 0:
        to_snafu(value//5, add_one)


to_snafu(total_value)
print("".join(val_list[::-1]))
