with open("inputs/input_day10_0.txt", 'r') as f:
    lines = f.readlines()

test_case = [
    "addx 15",
    "addx -11",
    "addx 6",
    "addx -3",
    "addx 5",
    "addx -1",
    "addx -8",
    "addx 13",
    "addx 4",
    "noop",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx -35",
    "addx 1",
    "addx 24",
    "addx -19",
    "addx 1",
    "addx 16",
    "addx -11",
    "noop",
    "noop",
    "addx 21",
    "addx -15",
    "noop",
    "noop",
    "addx -3",
    "addx 9",
    "addx 1",
    "addx -3",
    "addx 8",
    "addx 1",
    "addx 5",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx -36",
    "noop",
    "addx 1",
    "addx 7",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "addx 6",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx 7",
    "addx 1",
    "noop",
    "addx -13",
    "addx 13",
    "addx 7",
    "noop",
    "addx 1",
    "addx -33",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "noop",
    "noop",
    "noop",
    "addx 8",
    "noop",
    "addx -1",
    "addx 2",
    "addx 1",
    "noop",
    "addx 17",
    "addx -9",
    "addx 1",
    "addx 1",
    "addx -3",
    "addx 11",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx -13",
    "addx -19",
    "addx 1",
    "addx 3",
    "addx 26",
    "addx -30",
    "addx 12",
    "addx -1",
    "addx 3",
    "addx 1",
    "noop",
    "noop",
    "noop",
    "addx -9",
    "addx 18",
    "addx 1",
    "addx 2",
    "noop",
    "noop",
    "addx 9",
    "noop",
    "noop",
    "noop",
    "addx -1",
    "addx 2",
    "addx -37",
    "addx 1",
    "addx 3",
    "noop",
    "addx 15",
    "addx -21",
    "addx 22",
    "addx -6",
    "addx 1",
    "noop",
    "addx 2",
    "addx 1",
    "noop",
    "addx -10",
    "noop",
    "noop",
    "addx 20",
    "addx 1",
    "addx 2",
    "addx 2",
    "addx -6",
    "addx -11",
    "noop",
    "noop",
    "noop"
]

# lines = test_case


class CPU:
    def __init__(self):
        self.value = 1
        self.buffer = 0
        self.cycle = 1

    def draw_pixel(self):
        # Bij cycle meervoud van 40 gaf issues met de value, ivm value % 40 == 0, terwijl value 40 is.
        # Sorry not sorry.
        if not self.cycle % 40:
            if 38 <= self.value <= 42:
                return '#'
            else:
                return ' '
        if self.value <= self.cycle % 40 <= self.value + 2:
            return '#'
        else:
            return ' '

    def addx(self, value):
        self.buffer += value

    def noop(self):
        pass

    def update_cycle(self):
        self.cycle += 1

    def process_buffer(self):
        self.value += self.buffer
        self.buffer = 0

    def get_cycle(self):
        return self.cycle

    def get_signal_strength(self):
        if self.cycle in [20+i*40 for i in range(6)]:
            print(self.cycle)
            print(self.value)
            print(self.buffer)
            return self.cycle * self.value
        else:
            return 0

    def check_screen_end(self):
        if self.cycle in [i*40 for i in range(60)]:
            return '\n'

        else:
            return ''


print(lines)
cpu = CPU()
signal_strength = 0
for line in lines:
    if line[0:4] == 'addx':
        add_to_register = line.strip().split()[1]
        cpu.addx(value=int(add_to_register))
        cpu.update_cycle()
        signal_strength += cpu.get_signal_strength()
        cpu.update_cycle()
        cpu.process_buffer()
        signal_strength += cpu.get_signal_strength()
    else:
        cpu.noop()
        cpu.update_cycle()
        signal_strength += cpu.get_signal_strength()

cpu2 = CPU()
screen_pixels = ''
for line in lines:
    if line[0:4] == 'addx':
        add_to_register = line.strip().split()[1]
        cpu2.addx(value=int(add_to_register))
        screen_pixels += cpu2.draw_pixel()
        screen_pixels += cpu2.check_screen_end()
        cpu2.update_cycle()
        screen_pixels += cpu2.draw_pixel()
        screen_pixels += cpu2.check_screen_end()
        cpu2.update_cycle()
        cpu2.process_buffer()
    else:
        cpu2.noop()

        screen_pixels += cpu2.draw_pixel()
        screen_pixels += cpu2.check_screen_end()
        cpu2.update_cycle()

print(screen_pixels)
