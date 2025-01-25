from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def compute_fuel_mass(mass):
    incremental_fuel = (int(mass) // 3) - 2
    if incremental_fuel <= 0:
        return int(mass)
    elif incremental_fuel <= 6:
        return int(mass) + incremental_fuel
    else:
        return int(mass) + compute_fuel_mass(incremental_fuel)


def part_1(modules):
    total_fuel = 0
    for module in modules:
        total_fuel += (int(module) // 3) - 2
    print(f"Part 1: {total_fuel}")


def part_2(modules):
    total_fuel = 0
    for module in modules:
        total_fuel += compute_fuel_mass(int(module) // 3 - 2)
    print(f"Part 2: {total_fuel}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 3502510
    part_2(data)  # Correct answer: 5250885