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
        data (list[str]): The strings to extract numbers from (puzzle input)
        search_strings (dict[str, int]): Strings to search for (numbers)

    Returns:
        int: All of the found numbers summed
    """
    number_sum = 0

    for line in data:
        lowest_index = 999
        highest_index = -1
        first_number = -1
        last_number = -1
        for key, val in search_strings.items():
            l_idx = line.find(key)
            r_idx = line.rfind(key)
            if r_idx > highest_index:
                highest_index = r_idx
                last_number = val
            if l_idx != -1 and l_idx < lowest_index:
                lowest_index = l_idx
                first_number = val * 10

        number_sum += first_number + last_number

    return number_sum

def part_1_original_solution(data):
    found_number_sum = 0
    for line in data:
        for char in line:
            if char.isdigit():
                number = int(char) * 10
                break
        for char in reversed(line):
            if char.isdigit():
                number += int(char)
        found_number_sum += number

    print(f"Part 1 (original): {found_number_sum}")  # Correct answer: 55447


if __name__ == "__main__":
    data = read_input()
    part_1_original_solution(data)
    print(f"Part 1 (refactored): {find_and_sum_numbers(data, NUMBER_STRINGS)}")  # Correct answer: 55447
    print(f"Part 2: {find_and_sum_numbers(data, NUMBER_STRINGS | WORD_NUMBERS)}")  # Correct answer: 54706
