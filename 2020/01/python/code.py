from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    for x in data:
        for y in data:
            solution_flag = False
            if int(x) + int(y) == 2020:
                print(f"Part 1: {int(x) * int(y)}")
                solution_flag = True
                break
        if solution_flag:
            break


def part_2(data):
    for x in data:
        for y in data:
            for z in data:
                solution_flag = False
                if int(x) + int(y) + int(z) == 2020:
                    print(f"Part 2: {int(x) * int(y) * int(z)}")
                    solution_flag = True
                    break
            if solution_flag:
                break
        if solution_flag:
            break


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 538464
    part_2(data)  # Correct answer: 278783190