data = open("data/day10.txt").read().splitlines()

X = 1
cycle = 1
to_add = 0
total = 0
i = 0

crt = [["." for _ in range(40)] for _ in range(6)]

while i < len(data):
    if ((cycle - 20) % 40) == 0:
        total += (cycle * X)

    if cycle % 40 == 0:
        print("".join(crt[int((cycle - 20) / 40)]))

    row = int(cycle / 40)
    item = cycle % 40

    item -= 1
    #print("row:", row, "item:", item)
    if (item == X) or (item == X + 1) or (item == X - 1):
        crt[row][item] = "#"

    cycle += 1
    if to_add != 0:
        X += to_add
        to_add = 0
        continue

    l = data[i].split(" ")
    if l[0] == "addx":
        to_add = int(l[1])

    i += 1

print(total)
