from math import floor
from sys import *


class Monkey:
    def __init__(self, starting_items, operation, division_test, loc_one, loc_two):
        self.starting_items: [int] = starting_items
        self.operation = operation
        self.division_test = division_test
        self.loc_one = loc_one
        self.loc_two = loc_two


data = open("data/day11e.txt").read().splitlines()
monkey_list: [Monkey] = []

for i in range(4):
    items = [int(x[-2:]) for x in data[(i*7)+1].split(",")]
    operation = data[(i*7)+2].split(" ")[-2:]
    test = int(data[(i*7)+3].split(" ")[-1])
    loc_one = int(data[(i*7)+4].split(" ")[-1])
    loc_two = int(data[(i*7)+5].split(" ")[-1])

    m = Monkey(items, operation, test, loc_one, loc_two)
    monkey_list.append(m)

inspects = [0 for i in range(8)]
for round in range(10000):
    for m_num, monke in enumerate(monkey_list):
        for i, item in enumerate(monke.starting_items):
            inspects[m_num] += 1
            old = item
            op = f"{item} {monke.operation[0]} {monke.operation[1]}"
            monke.starting_items[i] = eval(op)
            #monke.starting_items[i] = floor(monke.starting_items[i])
            if monke.starting_items[i] % monke.division_test == 0:
                monkey_list[monke.loc_one].starting_items.append(monke.starting_items[i])
            else:
                monkey_list[monke.loc_two].starting_items.append(monke.starting_items[i])
        monke.starting_items = []
    # print(f"After round {round},")
    # for k, km in enumerate(monkey_list):
    #     print(f"Monkey {k}: {km.starting_items}")


inspects = sorted(inspects, reverse=True)
print(inspects)
print(inspects[0] * inspects[1])
# 54684, too low
