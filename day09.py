data = open("data/day09.txt").read().splitlines()


def is_touching(hs, ts):
    if abs(hs[0] - ts[0]) <= 1 and abs(hs[1] - ts[1]) <= 1:
        return True
    return False


def part_a():
    H_spot = [500, 500]
    T_spot = [500, 500]
    visits = [[0 for _ in range(1000)] for _ in range(1000)]
    visits[500][500] = 1
    # print(visits)
    for line in data:
        l = line.split(" ")
        match (l[0]):
            case "R":
                H_spot[0] += int(l[1])
            case "L":
                H_spot[0] -= int(l[1])
            case "D":
                H_spot[1] -= int(l[1])
            case "U":
                H_spot[1] += int(l[1])

        while not is_touching(H_spot, T_spot):
            print(f"T: {T_spot}, H: {H_spot}")
            if (H_spot[0] - T_spot[0] > 0) and (H_spot[1] == T_spot[1]):
                T_spot[0] += 1
            elif (H_spot[0] - T_spot[0] < 0) and (H_spot[1] == T_spot[1]):
                T_spot[0] -= 1
            elif (H_spot[1] - T_spot[1] > 0) and (H_spot[0] == T_spot[0]):
                T_spot[1] += 1
            elif (H_spot[1] - T_spot[1] < 0) and (H_spot[0] == T_spot[0]):
                T_spot[1] -= 1
            elif (H_spot[0] > T_spot[0]) and (H_spot[1] > T_spot[1]):  # Up-right
                T_spot[0] += 1
                T_spot[1] += 1
            elif (H_spot[0] < T_spot[0]) and (H_spot[1] < T_spot[1]):  # Bottom-left
                T_spot[0] -= 1
                T_spot[1] -= 1
            elif (H_spot[0] > T_spot[0]) and (H_spot[1] < T_spot[1]):  # Up-right
                T_spot[0] += 1
                T_spot[1] -= 1
            elif (H_spot[0] < T_spot[0]) and (H_spot[1] > T_spot[1]):  # Bottom-left
                T_spot[0] -= 1
                T_spot[1] += 1

            visits[T_spot[0]][T_spot[1]] = 1

    value = sum([sum(x) for x in visits])
    return value


def part_b():
    spots = [[500,500] for _ in range(10)]

    visits = [[0 for _ in range(1000)] for _ in range(1000)]
    visits[500][500] = 1
    # print(visits)
    for line in data:
        l = line.split(" ")
        match (l[0]):
            case "R":
                spots[0][0] += int(l[1])
            case "L":
                spots[0][0] -= int(l[1])
            case "D":
                spots[0][1] -= int(l[1])
            case "U":
                spots[0][1] += int(l[1])

        for i, knot in enumerate(spots[1:]):
            #print(i)
            while not is_touching(spots[i], knot):
                print(f"T: {knot}, H: {spots[i]}")
                if (spots[i][0] - knot[0] > 0) and (spots[i][1] == knot[1]):
                    knot[0] += 1
                elif (spots[i][0] - knot[0] < 0) and (spots[i][1] == knot[1]):
                    knot[0] -= 1
                elif (spots[i][1] - knot[1] > 0) and (spots[i][0] == knot[0]):
                    knot[1] += 1
                elif (spots[i][1] - knot[1] < 0) and (spots[i][0] == knot[0]):
                    knot[1] -= 1
                elif (spots[i][0] > knot[0]) and (spots[i][1] > knot[1]):  # Up-right
                    knot[0] += 1
                    knot[1] += 1
                elif (spots[i][0] < knot[0]) and (spots[i][1] < knot[1]):  # Bottom-left
                    knot[0] -= 1
                    knot[1] -= 1
                elif (spots[i][0] > knot[0]) and (spots[i][1] < knot[1]):  # Up-right
                    knot[0] += 1
                    knot[1] -= 1
                elif (spots[i][0] < knot[0]) and (spots[i][1] > knot[1]):  # Bottom-left
                    knot[0] -= 1
                    knot[1] += 1

                visits[spots[9][0]][spots[9][1]] = 1

    value = sum([sum(x) for x in visits])
    print(value)    #2223, 2224 too low


part_b()
