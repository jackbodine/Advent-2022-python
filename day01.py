data = open("data/day01.txt").read().splitlines()

calories = [0]
i = 0
for line in data[:-1]:
    if not line.isnumeric():
        i += 1
        calories.append(0)
    else:
        calories[i] += int(line)


print(sum(sorted(calories)[-3:]))