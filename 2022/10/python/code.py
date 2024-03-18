from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(program):
    x = 1
    signal_strength = 0
    cycle = 0

    for instruction in program:
        clean_inst = instruction.strip().split()
        if clean_inst[0] == "noop":
            cycles_to_add = 1
        else:
            cycles_to_add = 2

        for i in range(cycles_to_add):
            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strength += x * cycle
            if i == 1:
                x += int(clean_inst[1])

    print(f"Part 1: {signal_strength}")


def part_2(program):
    x = 1
    cycle = -1
    screen_buffer = [" " for _ in range(240)]

    for inst in program:
        instruction = inst.strip().split()[0]

        if instruction == "noop":
            cycles_to_add = 1
        else:
            cycles_to_add = 2

        for i in range(cycles_to_add):
            cycle += 1
            if cycle % 40 == 0 and cycle != 0:
                x += 40
            if cycle in [x - 1, x, x + 1]:
                screen_buffer[cycle] = "█"
            if i == 1:
                x += int(inst.strip().split()[1])

    print(f"Part 2:")
    print("".join(screen_buffer[0:40]))
    print("".join(screen_buffer[40:80]))
    print("".join(screen_buffer[80:120]))
    print("".join(screen_buffer[120:160]))
    print("".join(screen_buffer[160:200]))
    print("".join(screen_buffer[200:240]))


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 15120
    part_2(data)  # Correct answer: RKPJBPLA