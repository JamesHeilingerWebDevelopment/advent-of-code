from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def process_puzzle_input(input):
    # Separate the inputs
    raw_crates, raw_procedure = input.split("\n\n")

    # Process the crate information
    raw_crate_stacks = raw_crates.replace("    ", "[*]").replace(" ", "").split("\n")[:-1]
    temp_crate_stacks = []
    for line in raw_crate_stacks:
        temp_crate_stacks.append(line.strip("[").strip("]").split("]["))
    crate_stacks = [[] for _ in range(len(temp_crate_stacks[0]))]
    for line in temp_crate_stacks:
        for stack, crate in zip(crate_stacks, line):
            if crate != "*":
                stack.append(crate)

    # Process the procedure information
    procedure = []
    for instruction in raw_procedure.split("\n"):
        a = instruction.split(" ")
        procedure.append([int(a[1]), int(a[3]), int(a[5])])

    return crate_stacks, procedure


def part_1(crate_stacks, procedure):
    output = []
    for step in procedure:
        for move in range(step[0]):
            crane = crate_stacks[step[1]-1].pop(0)
            crate_stacks[step[2]-1].insert(0, crane)
    for stack in crate_stacks:
        output.append(stack.pop(0))

    print(f"Part 1: {''.join(output)}")


def part_2(crate_stacks, procedure):
    output = []
    for step in procedure:
        crane = []
        amt = step[0]
        start_stack = crate_stacks[step[1]-1]
        end_stack = crate_stacks[step[2]-1]
        for _ in range(amt):
            crane.extend(start_stack.pop(0))
        crane.reverse()
        end_stack.reverse()
        end_stack.extend(crane)
        end_stack.reverse()
    for stack in crate_stacks:
        output.append(stack.pop(0))
    print(f"Part 2: {''.join(output)}")


if __name__ == "__main__":
    part_1(*process_puzzle_input(read_input()))  # Correct answer: CVCWCRTVQ
    part_2(*process_puzzle_input(read_input()))  # Correct answer: CNSCZWLVT