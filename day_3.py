testinput = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

with open("inputs/input_day3_0.txt", 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]


def get_duplicate_letter(first_part, second_part):
    for letter in first_part:
        if letter in second_part:
            return letter


def convert_letter_to_number(letter):
    if letter.islower():
        return ord(letter)-96
    else:
        return ord(letter)-64+26


total_value = 0
for line in lines:
    print(line)
    print(len(line))
    halfway = int(len(line)/2)
    first_part = line[:halfway]
    second_part = line[halfway:]
    duplicate_letter = get_duplicate_letter(first_part, second_part)
    letter_value = convert_letter_to_number(duplicate_letter)
    total_value += letter_value
print(total_value)


def find_duplicate_letter(letter, list_1, list_2):
    if letter in list_1 and letter in list_2:
        return True


# new_lines = testinput
total_value_group = 0
for i in range(0, len(lines), 3):
    for letter in lines[i]:
        if find_duplicate_letter(letter, lines[i+1], lines[i+2]):
            letter_value = convert_letter_to_number(letter)
            print(letter, letter_value)
            total_value_group += letter_value
            break
print(total_value_group)
