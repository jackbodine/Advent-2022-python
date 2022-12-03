data = open("data/day03.txt").read().splitlines()


def get_priority(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


item_priorities = 0
badge_priorities = 0
for i, rucksack in enumerate(data):
    mid = int(len(rucksack) / 2)
    compartment_1 = rucksack[:mid]
    compartment_2 = rucksack[mid:]

    for item in compartment_1:
        if item in compartment_2:
            item_priorities += get_priority(item)
            break

    if i % 3 == 0:
        for c in data[i]:
            if (c in data[i + 1]) and (c in data[i + 2]):
                badge_priorities += get_priority(c)
                break

print(item_priorities)
print(badge_priorities)
