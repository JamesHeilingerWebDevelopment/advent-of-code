from collections import namedtuple
from sys import argv


Line = namedtuple("Line", ["inst", "num"])


def read_input():
    with open(argv[1], "r") as fp:
        raw = fp.read()
        return raw.split("\n")


def process_input(lines):
    program = []

    for line in lines:
        inst, val = line.split()
        program.append(Line(inst, int(val)))

    return program


def execute_program(program):
    accumulator = 0
    pointer = 0
    visited = []

    while True:
        if pointer >= len(program):
            return accumulator
        elif pointer not in visited:
            visited.append(pointer)
        else:
            return None

        line = program[pointer]
        if line.inst == "jmp":
            pointer += line.num
        elif line.inst == "acc":
            accumulator += line.num
            pointer += 1
        else:
            pointer += 1


def part_1(program):
    accumulator = 0
    pointer = 0
    visited = []

    while True:
        if pointer not in visited:
            visited.append(pointer)
        else:
            break

        line = program[pointer]
        if line.inst == "jmp":
            pointer += line.num
        elif line.inst == "acc":
            accumulator += line.num
            pointer += 1
        else:
            pointer += 1

    print(f"Part 1: {accumulator}")


def part_2(program: list):
    idx = 0
    while True:
        if program[idx].inst == "nop":
            test_program = program.copy()
            test_program[idx] = Line("jmp", test_program[idx].num)
            rval = execute_program(test_program)
            if rval is not None:
                break
        elif program[idx].inst == "jmp":
            test_program = program.copy()
            test_program[idx] = Line("nop", test_program[idx].num)
            rval = execute_program(test_program)
            if rval is not None:
                break
        idx += 1
    print(f"Part 2: {rval}")


if __name__ == "__main__":
    data = process_input(read_input())
    part_1(data)  # Correct answer: 1384
    part_2(data)  # Correct answer: 761