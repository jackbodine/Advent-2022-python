data = open("data/day02.txt").read().splitlines()


def part_a():
    draws = ["A X", "B Y", "C Z"]
    wins = ["A Y", "B Z", "C X"]
    score = 0

    for line in data:
        score += "XYZ".index(line[-1]) + 1
        if line in wins:
            score += 6
        elif line in draws:
            score += 3

    return score


def part_b():
    score = 0

    tie_dict = {
        "A": 0,
        "B": 1,
        "C": 2,
    }

    win_dict = {
        "A": 2,
        "B": 3,
        "C": 1,
    }

    lose_dict = {
        "A": 3,
        "B": 1,
        "C": 2,
    }

    for line in data:
        v = line.split(" ")
        s = tie_dict[v[0]] + "XYZ".index(v[-1])
        if s >= 3:
            s = (s % 3) + 1
        score += s
        if v[-1] == "Y":    # Draw
            score += 3
            #score += tie_dict[v[0]]
        elif v[-1] == "X":    # Lose
            score += 0
            #score += lose_dict[v[0]]
        elif v[-1] == "Z":  # Win
            score += 6
            #score += win_dict[v[0]]

    return score


print(part_a())
print(part_b())

# 14375
# 10274
