from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n\n")


def part_1(chunks):
    inventory = []
    for chunk in chunks:
        inventory.append(sum([int(x) for x in chunk.split("\n")]))

    top_inventory = []
    for i in range(3):
        top_inventory.append(max(inventory))
        inventory.remove(top_inventory[i])


    print(f"Part 1: {top_inventory[0]}")
    return top_inventory


def part_2(top_three):
    print(f"Part 2: {sum(top_three)}")


if __name__ == "__main__":
    # Part 1 answer: 74394
    # Part 2 answer: 212836
    part_2(part_1(read_input()))