from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def get_group_answers(s: str) -> list:
    return s.split("\n\n")


def part_1(groups):
    yes_count = 0
    for group in groups:
        yes_count += len(set("".join(group.strip("\n").split())))
    print(f"Part 1: {yes_count}")


def part_2(groups):
    yes_count = 0
    for group in groups:
        answers = [set(x) for x in group.split()]
        final = answers[0]
        if len(answers) > 1:
            for current in answers[1 : len(answers)]:
                final = final & current
        yes_count += len(final)
    print(f"Part 2: {yes_count}")


if __name__ == "__main__":
    data = get_group_answers(read_input())
    part_1(data)  # Correct answer: 6351
    part_2(data)  # Correct answer: 3143
