from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def consecutive_digit_check(val: str) -> bool:
    if (
        int(val[0]) == int(val[1])
        or int(val[1]) == int(val[2])
        or int(val[2]) == int(val[3])
        or int(val[3]) == int(val[4])
        or int(val[4]) == int(val[5])
    ):
        return True
    else:
        return False


def improved_consecutive_digit_check(val: str) -> bool:
    if "11" in val and "111" not in val:
        return True
    elif "22" in val and "222" not in val:
        return True
    elif "33" in val and "333" not in val:
        return True
    elif "44" in val and "444" not in val:
        return True
    elif "55" in val and "555" not in val:
        return True
    elif "66" in val and "666" not in val:
        return True
    elif "77" in val and "777" not in val:
        return True
    elif "88" in val and "888" not in val:
        return True
    elif "99" in val and "999" not in val:
        return True
    else:
        return False


def increase_only_check(val: str) -> bool:
    if (
        int(val[0])
        <= int(val[1])
        <= int(val[2])
        <= int(val[3])
        <= int(val[4])
        <= int(val[5])
    ):
        return True
    else:
        return False


def part_1(data):
    count = 0
    lower_bound, upper_bound = data.split("-")
    for num in range(int(lower_bound), int(upper_bound) + 1):
        if consecutive_digit_check(str(num)) and increase_only_check(str(num)):
            count += 1
    print(f"Part 1: {count}")


def part_2(data):
    count = 0
    lower_bound, upper_bound = data.split("-")
    for num in range(int(lower_bound), int(upper_bound) + 1):
        if increase_only_check(str(num)) and improved_consecutive_digit_check(str(num)):
            count += 1
    print(f"Part 2: {count}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 979
    part_2(data)  # Correct answer: 635