from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    good_count = 0
    for line in data:
        low, high = line.split()[0].split("-")
        password = line.split(": ")[1]
        letter = line.split(":")[0].split()[1]

        val = password.count(letter)
        if val >= int(low) and val <= int(high):
            good_count += 1

    print(f"Part 1: {good_count}")


def part_2(data):
    good_count = 0
    for line in data:
        pos1, pos2 = line.split()[0].split("-")
        password = line.split(": ")[1]
        letter = line.split(":")[0].split()[1]

        if password[int(pos1) - 1] == letter and password[int(pos2) - 1] != letter:
            good_count += 1
        elif password[int(pos1) - 1] != letter and password[int(pos2) - 1] == letter:
            good_count +=1

    print(f"Part 2: {good_count}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 447
    part_2(data)  # Correct answer: 249
