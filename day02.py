data = open("data/day02.txt").read().splitlines()


def part_a():
    draws = ["A X", "B Y", "C Z"]
    wins = ["A Y", "B Z", "C X"]
    score = 0

    for line in data:
        t_score = 0
        v = line.split(" ")
        if v[1] == "X":
            t_score += 1
        elif v[1] == "Y":
            t_score += 2
        elif v[1] == "Z":
            t_score += 3

        if line in wins:
            t_score += 6
        elif line in draws:
            t_score += 3

        score += t_score

    print(score)


def part_b():
    draws = ["A X", "B Y", "C Z"]
    wins = ["A Y", "B Z", "C X"]
    score = 0

    win_dict = {
        "A": 2,
        "B": 3,
        "C": 1,
    }

    tie_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    lose_dict = {
        "A": 3,
        "B": 1,
        "C": 2,
    }

    for line in data:
        t_score = 0
        v = line.split(" ")
        if v[-1] == "Y":    # Draw
            t_score += 3
            t_score += tie_dict[v[0]] + 1
        elif v[-1] == "X":    # Lose
            t_score += 0
            t_score += lose_dict[v[0]]
        elif v[-1] == "Z":  # Win
            t_score += 6
            t_score += (tie_dict[v[0]] + 1) % 3

        score += t_score

    print(score)

partb()
# 14375
# 10274