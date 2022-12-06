with open("inputs/input_day6_0.txt", 'r') as f:
    lines = f.read()

# Tests part 1:
# lines = "bvwbjplbgvbhsrlpgdmjqwftvncz" # Result should be 5
# lines= "nppdvjthqldpwncqszvftbrmjlhg" # Result should be 6
# lines = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # Result should be 10
# lines = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvj" # Result should be 11

# Tests part 2
# lines = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # Result should be 19
# lines = "bvwbjplbgvbhsrlpgdmjqwftvncz"  # Result should be 23
# lines = "nppdvjthqldpwncqszvftbrmjlh"  # Result should be 23
# lines = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprs"  # Result should be 29
# lines = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # Result should be 26

length_of_marker = 14  # from puzzle input --> 4 or 14.
length_of_starting_sequence = length_of_marker - 1
buffer = list(lines[0:length_of_starting_sequence])

for i, new_character in enumerate(lines[length_of_starting_sequence:]):
    buffer.append(new_character)
    if len(buffer) == len(set(buffer)):
        index_all_unique_chars = i + length_of_marker
        print(index_all_unique_chars, new_character)
        break
    else:
        buffer = buffer[1:]
