data = open("data/day06.txt").read()


def find_group(length):
    for i, c in enumerate(data):
        group = data[i:i+length]
        if len(set(group)) == len(group):
            return i + length


print(find_group(4))
print(find_group(14))
