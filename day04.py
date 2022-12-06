data = open("data/day04.txt").read().splitlines()

count = 0
overlap_count = 0
for line in data:
    pair = line.split(",")
    first = [int(x) for x in pair[0].split("-")]
    second = [int(x) for x in pair[1].split("-")]

    if first[0] <= int(second[0]) and first[1] >= int(second[1]) or int(second[0]) <= first[0] and (int(second[1]) >= first[1]):
        count += 1

    fs = set(range(first[0], first[1]+1))
    ss = set(range(second[0], second[1]+1))
    if len(ss & fs) > 0:
        overlap_count += 1

print(count)
print(overlap_count)
