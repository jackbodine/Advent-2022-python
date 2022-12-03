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

    item = set(rucksack[:mid]) & set(rucksack[mid:])
    item_priorities += get_priority(item.pop())

    if i % 3 == 0:
        badge = set(data[i]) & set(data[i + 1]) & set(data[i + 2])
        badge_priorities += get_priority(badge.pop())

print(item_priorities)
print(badge_priorities)
