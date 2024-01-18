import re
from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def get_symbol_indexes_for_row(row_data: str) -> list[int]:
    indexes = []
    indexes.extend(x.start() for x in re.finditer(r"[/+=*@#$%&-]", row_data))
    return indexes


def find_gear_indexes(row_data: str) -> list[int]:
    indexes = []
    indexes.extend(x.start() for x in re.finditer(r"[*]", row_data))
    return indexes


def is_part_number(num_index: int, symbol_indexes: list[int]) -> bool:
    """If the number indexes are adjacent to a symbol index, it's a part number.

    Args:
        num_index (int): Index for the digit of a number.
        sumbol_indexes (list[int]): Indexes for the part number symbols.

    Returns:
        bool: True if it is a part number, False if it isn't.
    """
    for j in symbol_indexes:
        if num_index == j - 1 or num_index == j or num_index == j + 1:
            return True
    return False


def part_1(data):
    total = 0

    for row_index in range(len(data)):
        number_indexes = [[x for x in range(i.start(), i.end())] for i in re.finditer(r"\d+", data[row_index])]
        for num_set in number_indexes:
            for num in num_set:
                if row_index - 1 >= 0:
                    symbol_indexes = get_symbol_indexes_for_row(data[row_index - 1])
                    if is_part_number(num, symbol_indexes):
                        total += int("".join([data[row_index][x] for x in num_set]))
                        break
                if row_index + 1 <= len(data) - 1:
                    symbol_indexes = get_symbol_indexes_for_row(data[row_index + 1])
                    if is_part_number(num, symbol_indexes):
                        total += int("".join([data[row_index][x] for x in num_set]))
                        break
                if row_index >= 0 and row_index <= len(data) - 1:
                    symbol_indexes = get_symbol_indexes_for_row(data[row_index])
                    if is_part_number(num, symbol_indexes):
                        total += int("".join([data[row_index][x] for x in num_set]))
                        break

    print(f"Part 1: {total}")


def part_2(data):
    total = 0

    for row_index in range(len(data)):
        for gear_idx in [x.start() for x in re.finditer(r"[*]", data[row_index])]:
            gear_vals = []
            if row_index - 1 >= 0:
                number_index_groups = [[x for x in range(i.start(), i.end())] for i in re.finditer(r"\d+", data[row_index - 1])]
                for number_group in number_index_groups:
                    if is_part_number(gear_idx, number_group):
                        gear_vals.append(int("".join([data[row_index - 1][x] for x in number_group])))
            if row_index + 1 <= len(data) - 1:
                number_index_groups = [[x for x in range(i.start(), i.end())] for i in re.finditer(r"\d+", data[row_index])]
                for number_group in number_index_groups:
                    if is_part_number(gear_idx, number_group):
                        gear_vals.append(int("".join([data[row_index][x] for x in number_group])))
            if row_index >= 0 and row_index <= len(data) - 1:
                number_index_groups = [[x for x in range(i.start(), i.end())] for i in re.finditer(r"\d+", data[row_index + 1])]
                for number_group in number_index_groups:
                    if is_part_number(gear_idx, number_group):
                        gear_vals.append(int("".join([data[row_index + 1][x] for x in number_group])))
            if len(gear_vals) == 2:
                total += int(gear_vals[0]) * int(gear_vals[1])
            elif len(gear_vals) > 2:
                print(gear_vals)
                raise

    print(f"Part 2: {total}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 537732
    part_2(data)  # Correct answer: 84883664