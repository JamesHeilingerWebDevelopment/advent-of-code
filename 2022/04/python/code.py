from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    output = 0
    for pair in data:
        a, b = pair.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        if (int(a1) <= int(b1) and int(a2) >= int(b2)) or (int(b1) <= int(a1) and int(b2) >= int(a2)):
            output += 1
    print(f"Part 1: {output}")


def part_2(data):
    output = 0
    for pair in data:
        a, b = pair.split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        if (int(b1) >= int(a1) and int(b1) <= int(a2)) or (int(b2) >= int(a1) and int(b2) <= int(a1)):
            output += 1
        elif (int(a1) >= int(b1) and int(a1) <= int(b2)) or (int(a2) >= int(b1) and int(a2) <= int(b1)):
            output += 1
    print(f"Part 2: {output}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 528
    part_2(data)  # Correct answer: 881