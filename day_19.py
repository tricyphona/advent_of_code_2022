test_input = [
    "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
"Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."
]

with open("inputs/input_day19_0.txt", 'r') as f:
    lines = f.readlines()


class BluePrint:
    options = 0
    def __init__(self, id,ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost):
        self.id = id
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost

    def __repr__(self):
        return f"{self.id}"

    def get_optimal_produce(
            self,
            production = None,
            ore = 1,
            clay = 0,
            obsidian = 0,
            geode = 0,
            ore_robots = 1,
            clay_robots = 0,
            obsidian_robots=0,
            geode_robots = 0,
            minute = 0
    ):
        if production is None:
            production = []
        self.all_the_actions(ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, minute, production)
        return production

    def all_the_actions(self, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, minute, production):
        print(minute)
        if minute >= 24:
            production.append(geode + geode_robots)
            BluePrint.options += 1
            print(BluePrint.options)
        if self.ore_robot_cost <= ore and minute < 24:
            self.all_the_actions(ore+ore_robots-self.ore_robot_cost, clay+clay_robots, obsidian+obsidian_robots, geode+geode_robots, ore_robots+1, clay_robots, obsidian_robots, geode_robots, minute+1,production)
        if self.clay_robot_cost <= ore and minute < 24:
            self.all_the_actions(ore+ore_robots-self.clay_robot_cost, clay+clay_robots, obsidian+obsidian_robots, geode+geode_robots, ore_robots, clay_robots+1, obsidian_robots, geode_robots, minute+1,production)
        if self.obsidian_robot_cost[0] < ore and self.obsidian_robot_cost[1] < clay and minute < 24:
            self.all_the_actions(ore+ore_robots-self.obsidian_robot_cost[0], clay+clay_robots - self.obsidian_robot_cost[1], obsidian+obsidian_robots, geode+geode_robots, ore_robots, clay_robots, obsidian_robots+1, geode_robots, minute+1, production)
        if self.geode_robot_cost[0] < ore and self.geode_robot_cost[1] < obsidian and minute < 24:
            self.all_the_actions(ore+ore_robots-self.geode_robot_cost[0], clay+clay_robots, obsidian+obsidian_robots-self.geode_robot_cost[1], geode+geode_robots, ore_robots, clay_robots, obsidian_robots, geode_robots+1, minute+1, production)
        if minute < 24:
            self.all_the_actions(ore + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, ore_robots, clay_robots, obsidian_robots, geode_robots, minute + 1, production)



lines=test_input
blue_prints = []

for line in lines:
    row = line.split(' ')
    blue_print_id = int(row[1].replace(':',''))
    ore_robot_cost = int(row[6])
    clay_robot_cost = int(row[12])
    obsidian_robot_cost = (int(row[18]),int(row[21]))
    geode_robot_cost = (int(row[-5]), int(row[-2]))
    blue_prints.append(BluePrint(blue_print_id, ore_robot_cost, clay_robot_cost, obsidian_robot_cost, geode_robot_cost))


print(blue_prints)

time_minutes = 24
print(blue_prints[1].ore_robot_cost)
print(blue_prints[1].clay_robot_cost)
print(blue_prints[1].obsidian_robot_cost)
print(blue_prints[1].geode_robot_cost)
print(blue_prints[0].get_optimal_produce())
