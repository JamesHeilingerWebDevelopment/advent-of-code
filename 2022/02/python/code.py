from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    total_score = 0
    shape_scoring = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    round_scoring = {
        "A Z": 0,
        "B X": 0,
        "C Y": 0,
        "A X": 3,
        "B Y": 3,
        "C Z": 3,
        "A Y": 6,
        "B Z": 6,
        "C X": 6
    }

    for line in data:
        _, me = line.split()
        total_score += shape_scoring[me] + round_scoring[line.strip()]

    print(f"Part 1: {total_score}")


def part_2(data):
    total_score = 0
    round_scoring = {
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "C Y": 3 + 3,
        "A X": 3 + 0,
        "B Y": 2 + 3,
        "C Z": 1 + 6,
        "A Y": 1 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0
    }

    for line in data:
        total_score += round_scoring[line.strip()]

    print(f"Part 2: {total_score}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 9177
    part_2(data)  # Correct answer: 1211