from collections import defaultdict

data = open("data/day07.txt").read().splitlines()

size_dict = defaultdict(lambda: 0)
wd = ""
for line in data[1:]:
    line_parts = line.split(" ")
    parents = wd.split("/")
    if line_parts[1] == "cd":
        if line_parts[-1] == "..":
            size = len(parents[-1]) + 1
            wd = wd[:-size]
        else:
            wd = wd + "/" + line_parts[-1]
    elif line_parts[0].isnumeric():
        for i, v in enumerate(parents):
            x = "".join(["/" + x for x in parents[:i + 1]])
            size_dict[x] += int(line_parts[0])
    elif line_parts[0] == "dir":
        size_dict[wd + line_parts[1]] = 0

print(sum([x for x in size_dict.values() if x <= 100000]))

# print(70000000 - 43313415)  # Unused space: 26686585
sorted_dict = dict(sorted(size_dict.items(), key=lambda item: item[1]))
for k, v in sorted_dict.items():
    if 26686585 + v >= 30000000:
        print(v)
        break