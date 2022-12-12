data = open("data/day08.txt").read().splitlines()

visible_trees = 0
for i in range(len(data)):
    highest = 0
    found_highest = False
    for j in range(len(data[i])):
        if found_highest:
            data[i][j] = "#"
        current_height = data[i][j]


print(visible_trees)