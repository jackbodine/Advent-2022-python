import re
data = open("data/day05.txt").read().splitlines()

stacks_r = [[] for i in range(10)]
index = data[8]

for line in data[:8]:
    for i, l in enumerate(line):
        if re.match("[a-zA-Z]", l):
            index = int((i-1)/4)
            stacks_r[index].append(l)

stacks = [list(reversed(x)) for x in stacks_r]

for line in data[10:]:
    v = line.split(" ")
    iterations = int(v[1])
    source = int(v[3]) - 1
    destination = int(v[5]) - 1
    for i in range(iterations):
        stacks[destination].append(stacks[source].pop())

# for i in stacks:
#     try:
#         print(i.pop())
#     except:
#         print(" ")



#
### PART 2
#
stacks_r = [[] for i in range(10)]
index = data[8]

for line in data[:8]:
    for i, l in enumerate(line):
        if re.match("[a-zA-Z]", l):
            index = int((i-1)/4)
            stacks_r[index].append(l)

stacks = [list(reversed(x)) for x in stacks_r]

for line in data[10:]:
    v = line.split(" ")
    iterations = int(v[1])
    source = int(v[3]) - 1
    destination = int(v[5]) - 1

    temp = []
    for i in range(iterations):
        temp.append(stacks[source].pop())

    stacks[destination] = stacks[destination] + list(reversed(temp))

for i in stacks:
    try:
        print(i.pop())
    except:
        print(" ")

