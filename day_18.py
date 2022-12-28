test_input = [
    "2,2,2",
    "1,2,2",
    "3,2,2",
    "2,1,2",
    "2,3,2",
    "2,2,1",
    "2,2,3",
    "2,2,4",
    "2,2,6",
    "1,2,5",
    "3,2,5",
    "2,1,5",
    "2,3,5"
]

with open("inputs/input_day18_0.txt", 'r') as f:
    lines = f.readlines()

# lines = test_input
print(lines)

rock_set = set()
max_x, max_y, max_z = 0,0,0
for line in lines:
    numbers = line.strip().split(',')
    if int(numbers[0]) > max_x:
        max_x = int(numbers[0])
    if int(numbers[1]) > max_y:
        max_y = int(numbers[1])
    if int(numbers[2]) > max_z:
        max_z = int(numbers[2])
    numbers = tuple(map(int, numbers))
    rock_set.add(numbers)
print(max_x)
print(max_y)
print(max_z)
print(len(rock_set))
print(rock_set)
def create_neighbours(rock):
    return (
        tuple((rock[0] - 1, *rock[1:])),
        tuple((rock[0] + 1, *rock[1:])),
        tuple((rock[0], rock[1] - 1, rock[2])),
        tuple((rock[0], rock[1] + 1, rock[2])),
        tuple((*rock[:2], rock[2] - 1)),
        tuple((*rock[:2], rock[2] + 1))
    )
side_of_rock_touching_other_rock=0
for rock in rock_set:
    neighbour_rocks = create_neighbours(rock)
    for neighbour_rock in neighbour_rocks:
        if neighbour_rock in rock_set:
            side_of_rock_touching_other_rock += 1
            print(side_of_rock_touching_other_rock)


print(len(rock_set) * 6 - side_of_rock_touching_other_rock)
# k=0
# for x in range(20):
#     for y in range(20):
#         for z in range(20):
#             air_pocket = (x,y,z)
#             if air_pocket not in rock_set:
#                 air_neighbours = create_neighbours(air_pocket)
#                 j = 0
#                 for air_neighbour in air_neighbours:
#                     if air_neighbour in rock_set:
#                         j+=1
#                 if j == 6:
#                     k += 1
# print(k)

# print((len(rock_set)*6 - i) - (k*6))

import numpy as np
lava_blob = np.zeros((30,30,30))
for rock in rock_set:
    lava_blob[rock] = 1

air_pockets = 0
air_pocket_list = []

def find_path_to_outside(air_pocket):
    visited = set()
    unvisisted_queue = set()
    unvisisted_queue.add(air_pocket)
    while len(unvisisted_queue):
        # print(unvisisted_queue)
        next_visit = unvisisted_queue.pop()
        visited.add(next_visit)
        # print(next_visit)
        neighbours = create_neighbours(next_visit)
        # print(f"Neighbours: {neighbours}")
        for neighbour in neighbours:
            if neighbour not in rock_set and neighbour not in visited:
                unvisisted_queue.add(neighbour)
            if 1 > any(neighbour) or any(neighbour) > max_value:
                return True
    return False
k=0
max_value = max(max_x, max_y, max_z)
for x in range(1,max_x+1):
    for y in range(1,max_y+1):
        for z in range(1,max_z+1):
            air_pocket = (x,y,z)
            if air_pocket not in rock_set:
                print(x,y,z)
                if not find_path_to_outside(air_pocket):
                    air_pocket_list.append((x,y,z))
                    trapped_air = create_neighbours(air_pocket)
                    for trapped_air_bubble in trapped_air:
                        if trapped_air_bubble in rock_set:
                            print(trapped_air_bubble)
                            k += 1


print(len(rock_set))
print(side_of_rock_touching_other_rock)
print(k)
print((len(rock_set) * 6 - side_of_rock_touching_other_rock) - (k))


# Het is traag, beter was om eerst te kijken welke air droplets in een rechte lijn met de buitenkant in contact stonden
# En als er een pad is naar 'buiten', toe te voegen aan een globale set zodat deze niet steeds opnieuw gemaakt wordt.
# It aint pretty, but it works (als je de tijd hebt).
