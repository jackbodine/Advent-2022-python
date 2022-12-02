data = open("data/day01.txt").read().splitlines()

calories: [int] = [0]
i: int = 0
for line in data[:-1]:
    if line.isnumeric():
        calories[i] += int(line)
    else:
        i += 1
        calories.append(0)

print(max(calories))
print(sum(sorted(calories)[-3:]))
