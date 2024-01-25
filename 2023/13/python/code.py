from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n\n")


def find_vertical_symmetry_lines(lines) -> list:
    possible_vertical_lines_of_symmetry = []
    for line in lines:
        vertical_lines = []
        for i in range(1, len(line)):
            if i <= len(line) // 2:
                if line[:i] == line[i:i+i][::-1]:
                    vertical_lines.append(i)
            else:
                if line[i-len(line[i:]):i] == line[i:][::-1]:
                    vertical_lines.append(i)
        possible_vertical_lines_of_symmetry.append(vertical_lines)
    return list(set.intersection(*map(set, possible_vertical_lines_of_symmetry)))


def find_horizontal_symmerty_lines(lines) -> list:
    possible_horizontal_lines_of_symmetry = []
    horizontal_lines = []
    for i in range(1, len(lines)):
        if i <= len(lines) // 2:
            if lines[:i] == lines[i:i+i][::-1]:
                horizontal_lines.append(i)
        else:
            if lines[i-len(lines[i:]):i] == lines[i:][::-1]:
                horizontal_lines.append(i)
        possible_horizontal_lines_of_symmetry.append(horizontal_lines)
    return list(set.intersection(*map(set, possible_horizontal_lines_of_symmetry)))


def find_symmetry_lines(section):
    lines = section.split("\n")
    return find_vertical_symmetry_lines(lines), find_horizontal_symmerty_lines(lines)


def modified_section_generator(section_list):
    for idx, item in enumerate(section_list):
        if item == ".":
            section_list[idx] = "#"
            yield "".join(section_list)
            section_list[idx] = "."
        elif item == "#":
            section_list[idx] = "."
            yield "".join(section_list)
            section_list[idx] = "#"


def part_1(data):
    start_time = time()
    total = 0
    for section in data:
        v, h = find_symmetry_lines(section)
        if v:
            total += v[0]
        elif h:
            total += h[0] * 100

    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def part_2(data):
    start_time = time()
    total = 0
    for section in data:
        old_symmetry_val = find_symmetry_lines(section)

        for modified_section in modified_section_generator(list(section)):
            break_flag = False
            v, h = find_symmetry_lines(modified_section)
            for x in v:
                if old_symmetry_val[0] and x != old_symmetry_val[0][0] or old_symmetry_val[0] == []:
                    total += x
                    break_flag = True
                    break
            if break_flag:
                break
            for y in h:
                if old_symmetry_val[1] and y != old_symmetry_val[1][0] or old_symmetry_val[1] == []:
                    total += (y * 100)
                    break_flag = True
                    break
            if break_flag:
                break

    print(f"Part 2: {total} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 27505
    part_2(data)  # Correct answer: 22906