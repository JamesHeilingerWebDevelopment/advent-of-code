from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        d = fp.read()
    d_val = d.split(",")
    return [int(x) for x in d_val]


def intcode_cpu(program):
    for i in range(0, len(program), 4):
        instruction = program[i]
        if instruction == 1:
            # add
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif instruction == 2:
            # multiply
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        elif instruction == 99:
            # terminate program
            break
    return program



def part_1(data):
    data = [data[0], 12, 2] + data[3:]
    print(f"Part 1: {intcode_cpu(data)[0]}")


def part_2(data):
    breakout_flag = False
    for i in range(100):
        for j in range(100):
            updated_data = data[:]
            updated_data[1] = i
            updated_data[2] = j
            output = intcode_cpu(updated_data)
            if output[0] == 19690720:
                breakout_flag = True
                break
        if breakout_flag:
            break
    print(f"Part 2: noun = {updated_data[1]}, verb = {updated_data[2]}, result = {100 * updated_data[1] + updated_data[2]}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 3716293
    part_2(data)  # Correct answer: 6429