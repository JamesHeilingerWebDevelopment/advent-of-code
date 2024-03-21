from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    increments = 0
    max_idx = len(data)
    for idx in range(1, max_idx):
        if (int(data[idx]) - int(data[idx-1])) >= 0:
            increments += 1
    print(f"Part 1: {increments}")


def part_2(data):
    increments = 0
    prev_window = sum([int(data[0]), int(data[1]), int(data[2])])
    for idx in range(3, len(data)):
        next_window = sum([int(data[idx-2]), int(data[idx-1]), int(data[idx])])
        if next_window - prev_window > 0:
            increments += 1
        prev_window = next_window
    print(f"Part 2: {increments}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 1162
    part_2(data)  # Correct answer: 1190