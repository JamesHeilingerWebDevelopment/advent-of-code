from sys import argv


def create_priorities():
    output = {}
    count = 1
    for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        output[letter] = count
        count += 1
    return output


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(rucksacks):
    priority_total = 0
    priorities = create_priorities()
    for sack in rucksacks:
        p1 = sack[0:len(sack)//2]
        p2 = sack[len(sack)//2:]
        for item in p1:
            if item in p2:
                priority_total += priorities[item]
                break
    print(f"Part 1: {priority_total}")


def part_2(rucksacks):
    priority_total = 0
    priorities = create_priorities()
    idx = 0
    while True:
        try:
            sack1 = rucksacks[idx].strip()
            sack2 = rucksacks[idx+1]
            sack3 = rucksacks[idx+2]
            for item in sack1:
                if item in sack2 and item in sack3:
                    priority_total += priorities[item]
                    break
        except IndexError:
            break
        idx += 3
    print(f"Part 2: {priority_total}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 7766
    part_2(data)  # Correct answer: 2415