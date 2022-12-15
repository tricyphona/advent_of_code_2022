import numpy as np
with open("inputs/input_day15_0.txt", 'r') as f:
    lines = f.readlines()

test_input = [
    "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3"]

# lines = test_input

class Sensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.beacon = None
        self.distance = 0

    def get_distance_sensor_beacon(self):
        self.distance = abs(self.x-self.beacon.x) + abs(self.y-self.beacon.y)
        return abs(self.x-self.beacon.x) + abs(self.y-self.beacon.y)

    def __repr__(self):
        return f"Sensor: {self.x}, {self.y}"

class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def beacon_in_row(self, row):
        return self.y == row

    def __repr__(self):
        return f"beacon: {self.x}, {self.y}"


class Range_scanned:
    def __init__(self, x_min=None, x_max=None):
        self.x_min = x_min
        self.x_max = x_max

    def overlap(self, x_min_range, x_max_range, edit=True):
        if self.x_min <= x_min_range and self.x_max >= x_max_range:
            pass
        elif self.x_min > x_min_range and self.x_max < x_max_range:
            if edit:
                self.x_min = x_min_range
                self.x_max = x_max_range
        elif self.x_min >= x_min_range and self.x_max >= x_max_range and self.x_min <= x_max_range:
            if edit:
                self.x_min = x_min_range
        elif self.x_min <= x_min_range and self.x_max <= x_max_range and self.x_max >= x_min_range:
            if edit:
                self.x_max = x_max_range
        else:
            return False
        return True

    def overlap_ranges(self, x_min_range, x_max_range, edit=True):
        if self.x_min <= x_min_range and self.x_max >= x_max_range:
            pass
        elif self.x_min > x_min_range and self.x_max < x_max_range:
            if edit:
                self.x_min = x_min_range
                self.x_max = x_max_range
        elif self.x_min >= x_min_range and self.x_max >= x_max_range and self.x_min <= x_max_range:
            if edit:
                self.x_min = x_min_range
        elif self.x_min <= x_min_range and self.x_max <= x_max_range and self.x_max >= x_min_range:
            if edit:
                self.x_max = x_max_range
        elif self.x_max+1 == x_min_range:
            self.x_max = x_max_range
        elif self.x_min-1 == x_max_range:
            self.x_min = x_min_range
        else:
            return False
        return True

    def __repr__(self):
        return f"{self.x_min} -- {self.x_max}"

sensors = []
beacons = []
def get_min_max(value, min, max):
    if not min < value < max:
        if min > value:
            min = value
        if max < value:
            max = value
    return min, max
sensor_min_x, sensor_min_y = 100000000, 100000000
sensor_max_x, sensor_max_y = 0, 0
for line in lines:
    line_input = line.split()
    sensor_x = int(line_input[2].split("=")[1].split(",")[0])
    sensor_min_x, sensor_max_x = get_min_max(sensor_x, sensor_min_x, sensor_max_x)
    sensor_y = int(line_input[3].split("=")[1].split(":")[0])
    sensor_min_y, sensor_max_y = get_min_max(sensor_y, sensor_min_y, sensor_max_y)
    sensors.append(Sensor(sensor_x, sensor_y))
    beacon_x = int(line_input[-2].split("=")[1].split(",")[0])
    beacon_y = int(line_input[-1].split("=")[1].split(":")[0])
    beacons.append(Beacon(beacon_x, beacon_y))
    sensors[-1].beacon = beacons[-1]

print(sensors)
print(beacons)
print(sensor_min_x, sensor_max_x, sensor_min_y, sensor_max_y)
# max_distance = 0
# for sensor in sensors:
#     if max_distance < sensor.get_distance_sensor_beacon():
#         max_distance = sensor.get_distance_sensor_beacon()
# max_y = sensor_max_y + max_distance
# min_y = sensor_min_y - max_distance
# max_x = sensor_max_x + max_distance
# min_x = sensor_min_x - max_distance

#part 2:
min_x, max_x = 0, 4000000
min_y, max_y = 0, 4000000
# for row_to_check in range(min_y, max_y):
#     print(row_to_check)
#     beacons_found = set()
#     relevant_sensors = set()
#     for sensor in sensors:
#         if sensor.y - sensor.distance <= row_to_check <= sensor.y + sensor.distance:
#             relevant_sensors.add(sensor)
#     for beacon in beacons:
#         if beacon.beacon_in_row(row_to_check):
#             beacons_found.add(beacon.x)
#     # print(relevant_sensors)
#     for x in range(min_x, max_x):
#         if x not in beacons_found:
#             for sensor in relevant_sensors:
#                 distance_to_x = abs(sensor.x - x) + abs(sensor.y - row_to_check)
#                 if distance_to_x <= sensor.distance:
#                     print(f"{x} is niet bacon succes!")
#                     no_beacon_found = True
#                     break

def remove_obsolete_ranges(scanned_ranges):
    ranges = [scanned_ranges[0]]
    for scanned_range in scanned_ranges:
        for range_scan in ranges:
            if range_scan.overlap_ranges(scanned_range.x_min, scanned_range.x_max):
                pass
            else:
                ranges.append(scanned_range)
    return ranges


max_row = 4000000
# max_row = 20
row = 2000000


def find_sensors(sensors, row):
    range_x_sensor = []
    for sensor in sensors:
        sensor.get_distance_sensor_beacon()
        range_x = sensor.distance - abs(row - sensor.y)
        if range_x >= 0:
            sensor_min_x = sensor.x - range_x
            sensor_max_x = sensor.x + range_x
            range_x_sensor.append([sensor_min_x, sensor_max_x])
    return range_x_sensor

def scan_x_range(range_x_sensor, scanned_ranges, row):
    for range_sensor in range_x_sensor:
        range_found = False
        for range_scanner in scanned_ranges:
            outcome = range_scanner.overlap(range_sensor[0], range_sensor[1])
            if outcome:
                range_found = True
        if not range_found:
            scanned_ranges.append(Range_scanned(range_sensor[0], range_sensor[1]))
    scanned_range_set = remove_obsolete_ranges(scanned_ranges)
    if len(scanned_range_set) > 1:
        print(row)
        print(scanned_range_set)


for row in range(0, max_row):
    range_x_sensor = find_sensors(sensors, row)
    scanned_ranges = [Range_scanned(range_x_sensor[0][0], range_x_sensor[0][1])]
    scan_x_range(range_x_sensor, scanned_ranges, row)
