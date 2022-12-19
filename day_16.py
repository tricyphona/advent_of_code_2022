import itertools
import math
with open("inputs/input_day16_0.txt", 'r') as f:
    lines = f.readlines()

test_input = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II"
    ]

# lines = test_input


class Valve:
    def __init__(self, name, flow_rate, tunnels_connected=[]):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels_connected = tunnels_connected
        self.weight = 1000

    def open_valve(self, minutes):
        minutes += 1
        return self.flow_rate, minutes

    def move(self, direction, minutes, valves):
        minutes += 1
        return valves[direction], minutes

    def __repr__(self):
        return f"{self.name}"

    def get_distance_to_tunnel(self, destination):
        unvisited = set()
        unvisited.add(self)
        self.weight = 0
        visited = set()
        while len(unvisited):
            # print(unvisited)
            next_visit = unvisited.pop()
            visited.add(next_visit)
            tunnels = next_visit.tunnels_connected
            for tunnel in tunnels:
                other_tunnel = valves[tunnel]
                if other_tunnel.weight > next_visit.weight:
                    other_tunnel.weight = next_visit.weight + 1
                    unvisited.add(other_tunnel)
        weight = valves[destination].weight
        for tunnel in visited:
            tunnel.weight = 1000
        return weight

valves = dict()
for line in lines:
    line_valve_input = line.split()
    name = line_valve_input[1]
    flow = int(line_valve_input[4].split('=')[-1][0:-1])
    connected_valves = [x.strip(',') for x in line_valve_input[9:]]
    valves[name] = Valve(name, flow,connected_valves)

start_valve = valves['AA']
valve = start_valve
valves_of_interest = [valve for dict_key, valve in valves.items() if valve.flow_rate > 0]

# print(valves_of_interest)
temp_list = []
minutes = 0
pressure = 0
max_minutes = 30


def get_cost_between_start_end(start_valve, valves_of_interest):
    temp_dict = dict()
    for interest_valve in valves_of_interest:
        cost = start_valve.get_distance_to_tunnel(interest_valve.name) + 1
        flow = interest_valve.flow_rate
        temp_dict[interest_valve.name] = cost, flow
    return temp_dict


#initial values:
max_minutes = 30
minutes = 0
pressure = 0


def process_time(start_valve, valves_costs, valve_key, minutes, pressure, max_minutes, valves_of_interest):
    minutes += valves_costs[valve_key][0]
    flow = valves_costs[valve_key][1]
    if minutes < max_minutes:
        pressure += flow * (max_minutes - minutes)
    valves_look_into = valves_of_interest[:]
    valves_look_into.remove(valves[valve_key])
    start_valve = valves[valve_key]
    if minutes < max_minutes and len(valves_look_into) > 0:
        # print(minutes, pressure)
        get_flow(start_valve, minutes, max_minutes, valves_look_into, pressure)
    else:
        if pressure > 1580:
            answer.append(pressure)
        else:
            answer.append(pressure)

answer = []
def get_flow(start_valve, minutes, max_minutes, valves_of_interest, pressure):
    valves_costs = get_cost_between_start_end(start_valve, valves_of_interest)
    for valve_key in valves_costs.keys():
        process_time(start_valve, valves_costs, valve_key, minutes, pressure, max_minutes, valves_of_interest)

# get_flow(start_valve, minutes, max_minutes, valves_of_interest, pressure)
# print(answer)
# print(max(answer))
    # return temp_list
# while len(valves_of_interest) > 0:
#     temp_list = []
#     temp_list = get_cost_between_start_end(start_valve, valves_of_interest)
#     max_value = 0
#     value = 0
#     for valve_inspected, value in temp_list:
#         if value > max_value:
#             max_value = value
#             true_valve = valve_inspected
#     valves_of_interest.remove(true_valve)
#     cost = start_valve.get_distance_to_tunnel(true_valve.name)
#     minutes += cost + 1
#     flow = true_valve.flow_rate
#     pressure += flow * (max_minutes - minutes)
#     start_valve = true_valve

# print(get_cost_between_start_end(start_valve, valves_of_interest))

# max_minutes = 30
# minute = 0
# i=0
# pressure = 0
# stop = False
# while minute < max_minutes:
#     options_per_tunnel = dict()
#     for tunnel_name in start_valve.tunnels_connected:
#         if len(valves_of_interest) == 0:
#             stop = True
#             break
#         tunnel = valves[tunnel_name]
#         options = get_cost_between_start_end(tunnel, valves_of_interest)
#         max_value = max(options.keys())
#         direction = options[max(options.keys())]
#         options_per_tunnel[max_value] = tunnel_name, direction
#     if stop:
#         break
#     max_value = max(options_per_tunnel.keys())
#
#     next_tunnel, direction = options_per_tunnel[max_value]
#     print(get_cost_between_start_end(start_valve, valves_of_interest))
#     print(direction)
#     minute += 1
#     print(valves[next_tunnel] == direction)
#     if valves[next_tunnel] in valves_of_interest and valves[next_tunnel] == direction and minute < 30:
#         valves_of_interest.remove(valves[next_tunnel])
#         minute += 1
#         pressure += valves[next_tunnel].flow_rate * (max_minutes - minute)
#         print("OPEN", minute, pressure)
#     print(valves_of_interest)
#     print(valves[next_tunnel])
#     start_valve = valves[next_tunnel]
# print(pressure)



#
# print("\nVanaf DD:")
# for tunnel_name in start_valve.tunnels_connected:
#     tunnel = valves[tunnel_name]
#     print(tunnel_name)
#     print(get_cost_between_start_end(tunnel, valves_of_interest))
# input()
# print("\nVANAF AA:")
# start_valve = valves['AA']
# for tunnel_name in start_valve.tunnels_connected:
#     tunnel = valves[tunnel_name]
#     print(tunnel_name)
#     print(get_cost_between_start_end(tunnel, valves_of_interest))
# valves_of_interest.remove(valves['BB'])
# print("\nVANAF BB:")
# start_valve = valves['BB']
# for tunnel_name in start_valve.tunnels_connected:
#     tunnel = valves[tunnel_name]
#     print(tunnel_name)
#     print(get_cost_between_start_end(tunnel, valves_of_interest))
# print("\nVANAF AA:")
# start_valve = valves['AA']
# for tunnel_name in start_valve.tunnels_connected:
#     tunnel = valves[tunnel_name]
#     print(tunnel_name)
#     print(get_cost_between_start_end(tunnel, valves_of_interest))
# print("\nVANAF II: ")
# start_valve = valves['II']
# for tunnel_name in start_valve.tunnels_connected:
#     tunnel = valves[tunnel_name]
#     print(tunnel_name)
#     print(get_cost_between_start_end(tunnel, valves_of_interest))
#

# if True:
#     valves_of_interest.remove(valves['DD'])
# print()
# for interest_valve in valves_of_interest:
#     print(interest_valve, valves['DD'].get_distance_to_tunnel(interest_valve.name), interest_valve.flow_rate)
# valves_of_interest.remove(valves['BB'])
# print()
# for interest_valve in valves_of_interest:
#     print(interest_valve, valves['BB'].get_distance_to_tunnel(interest_valve.name), interest_valve.flow_rate)
#
# valves_of_interest.remove(valves['JJ'])
# print()
# for interest_valve in valves_of_interest:
#     print(interest_valve, valves['JJ'].get_distance_to_tunnel(interest_valve.name), interest_valve.flow_rate)
#
# valves_of_interest.remove(valves['HH'])
# print()
# for interest_valve in valves_of_interest:
#     print(interest_valve, valves['HH'].get_distance_to_tunnel(interest_valve.name), interest_valve.flow_rate)

# total_flow = 0
# opened_valves = set()
# total_flow_rate = 0
# pressure_released = 0

# print(valve.get_distance_to_tunnel(destination))
# reward = valves[destination].flow_rate

# path = [start_valve]
# print(start_valve.get_distance_to_tunnel('DD'))

# def highest_efficienty(valves_of_interest, start_valve):
#     most_effect = 0
    # for valve in valves_of_interest:
    #     cost = start_valve.get_distance_to_tunnel(valve.name)
    #
    #     cost = start_valve.get_distance_to_tunnel(valve.name) + 1
    #     reward = valve.flow_rate
    #     effect = reward / cost
    #     if effect >= most_effect:
    #         most_effect = effect
    #         best_valve = valve
    # return most_effect, best_valve

# valve = start_valve
# def move_to_tunnels(valves_of_interest, start_valve, minute, path, all_pressures):
    # for valve in valves_of_interest:
    #     path2 = path.copy()
    #     valves_of_interest_copy = valves_of_interest.copy()
    #     cost = start_valve.get_distance_to_tunnel(valve.name)
    #     if cost + minute >= 30:
    #         pressure = 0
    #         for valve_flow, minute, _valve in path2:
    #             pressure += valve_flow * (30 - minute)
    #         return pressure
    #     minute += cost
    #     flow, minute = valve.open_valve(minute)
    #     valves_of_interest_copy.remove(valve)
    #     path2.append((flow, minute, valve))
    #
    #
    #     if minute <= 30 and len(valves_of_interest_copy):
    #         pressure = move_to_tunnels(valves_of_interest_copy, valve, minute, path2, all_pressures)
    #     else:
    #         pressure = 0
    #         for valve_flow, minute, _valve in path2:
    #             pressure += valve_flow * (30 - minute)
    #         return pressure
    # all_pressures.append(pressure)


#
# all_pressure = []
# # combinations = itertools.permutations(valves_of_interest)
# start_valve = valves['AA']
# max_minutes = 30
# length_combinations = math.factorial(len(valves_of_interest))

# for i, path in enumerate(combinations):
#     print(f"{i} / {length_combinations}")
#     minutes = 0
#     valve = start_valve
#     pressure = 0
#     for next_valve in path:
#         cost = valve.get_distance_to_tunnel(next_valve.name)
#         valve = next_valve
#         minutes += cost
#         if minutes < max_minutes:
#             flow, minutes = next_valve.open_valve(minutes)
#             pressure += flow * (max_minutes - minutes)
#             # print(valve.name, flow, pressure)
#     all_pressure.append(pressure)
#     # print(pressure)
#     # print(path)

# print(max(all_pressure))
# print(max(all_pressure))
#
#
# all_pressures = []
# total_pressure = []
# value = move_to_tunnels(valves_of_interest, start_valve, 0,[], all_pressures)


# class Score:
#     def __init__(self):
#         self.total_pressure_released = 0
# total_score = Score()
# def options(valve, minutes, total_flow, valves, opened_valves, total_flow_rate, pressure_released, total_score):
#     pressure_released += total_flow_rate
#     print(f"{minutes}: {valve}")
#     if minutes >= 30:
#         if pressure_released > total_score.total_pressure_released:
#             total_score.total_pressure_released = pressure_released
#             if int(pressure_released) == 1651:
#                 total_score.total_pressure_released
#     if valve.flow_rate > 0 and valve not in opened_valves:
#         flow_rate, minutes = valve.open_valve(minutes)
#         total_flow_rate += flow_rate
#         opened_valves.add(valve)
#         if minutes <= 30:
#             options(valve, minutes, total_flow, valves, opened_valves, total_flow_rate, pressure_released, total_score)
#     for tunnel in valve.tunnels_connected:
#         valve, minutes = valve.move(tunnel, minutes, valves)
#         if minutes <= 30:
#             options(valve, minutes, total_flow, valves, opened_valves,total_flow_rate, pressure_released, total_score)
#
# max_score = options(valve, 0, total_flow, valves, opened_valves, total_flow_rate, pressure_released, total_score)
# print(max_score)


path = dict()
print(valves_of_interest)
valves_of_interest_dict = valves_of_interest[:]
valves_of_interest_dict.append(valves['AA'])
for valve in valves_of_interest_dict:
    path[valve.name] = dict()
    for interest_valve in valves_of_interest:
        if interest_valve != valve:
            cost = valve.get_distance_to_tunnel(interest_valve.name) + 1
            flow = interest_valve.flow_rate
            path[valve.name][interest_valve.name] = {'cost': cost, 'flow': flow}
print(path)
# print(path['HT'])
pressure_list = []
old_pressure = []
i = 0
def open_valves(start_valve, available_valves, minute, minute2, pressure,i, route):
    for next_valve in available_valves:

        i += 1
        if pressure > 1050:
            old_pressure.append((pressure, route))
        if minute + path[start_valve.name][next_valve.name]['cost'] < 26:
            valves_to_go = available_valves[:]
            valves_to_go.remove(valves[next_valve.name])
            open_valves(next_valve, valves_to_go, minute + path[start_valve.name][next_valve.name]['cost'], minute2, pressure + (26-minute - path[start_valve.name][next_valve.name]['cost'])*path[start_valve.name][next_valve.name]['flow'],i, route+next_valve.name)
        pressure_list.append((int(pressure), route))


start_valve = valves['AA']
route = str()
open_valves(start_valve, valves_of_interest, 0,0, 0,i, route)
print(pressure_list)
try:
    print(max(pressure_list))
except:
    pass
print(old_pressure)
print(valves_of_interest)
pressure_list_part2 = old_pressure[:]

# elif minute2 + path[start_valve.name][next_valve.name]['cost'] < 26:
# valves_to_go = available_valves[:]
# valves_to_go.remove(valves[next_valve.name])
# open_valves(next_valve, valves_to_go, minute, minute2 + path[start_valve.name][next_valve.name]['cost'],
#             pressure + (26 - minute2 - path[start_valve.name][next_valve.name]['cost']) *
#             path[start_valve.name][next_valve.name]['flow'], i)

visited = old_pressure[0][1]
print(len(old_pressure))
largest_pressure = [0]
for j in range(len(pressure_list_part2)):
    # print(j)
    valves_of_interest3 = valves_of_interest[:]
    for i in range(0,len(pressure_list_part2[j][1]),2):
        valves_of_interest3.remove(valves[pressure_list_part2[j][1][i:i+2]])
    start_valve = valves['AA']
    pressure_list = []
    i = 0
    pressure_list2 = []
    route = str()
    open_valves(start_valve, valves_of_interest3, 0,0, 0,i, route)

    if pressure_list_part2[j][0] + max(pressure_list)[0] >= largest_pressure[0]:
        largest_pressure = (pressure_list_part2[j][0] + max(pressure_list)[0], pressure_list_part2[j][1], max(pressure_list)[1])
        print("NEW HIGHSCORE")
        print(pressure_list_part2[j][0])
        print(pressure_list_part2[j][1])
        print(max(pressure_list)[0])
        print(max(pressure_list)[1])
        print(largest_pressure)
print()
print(1160+864)
print(1266+930)
print(2031)
print(2084)
print(max(old_pressure))
print(largest_pressure[0])
print(largest_pressure)