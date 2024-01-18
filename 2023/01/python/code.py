from sys import argv


NUMBER_STRINGS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
WORD_NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def read_input():
    with open(argv[1], "r") as fp:
        file_input = fp.read()
        return file_input.split()


def find_and_sum_numbers(data: list[str], search_strings: dict[str, int]) -> int:
    """Find the first and last numbers in each string, combine into a number and return the sum.

    Args:
        data (list[str]): The strings to extract numbers from (puzzle input).
        search_strings (dict[str, int]): Strings to search for.

    Returns:
        int: All of the numbers summed.
    """
    number_sum = 0

    for line in data:
        lowest_index = 999
        highest_index = -1
        first_number = -1
        last_number = -1
        for k, v in search_strings.items():
            l_idx = line.find(k)
            r_idx = line.rfind(k)
            if r_idx > highest_index:
                highest_index = r_idx
                last_number = v
            if l_idx != -1 and l_idx < lowest_index:
                lowest_index = l_idx
                first_number = v * 10

        number_sum += first_number + last_number

    return number_sum


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {find_and_sum_numbers(data, NUMBER_STRINGS)}")  # Correct answer: 55447
    print(f"Part 2: {find_and_sum_numbers(data, NUMBER_STRINGS | WORD_NUMBERS)}")  # Correct answer: 54706