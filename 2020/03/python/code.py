from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def slope_location_generator(data, right, down):
    x = 0
    y = 0
    while y < len(data):
        yield data[y][x]
        x = (x + right) % 31
        # x = (x + right) % 11
        y += down


def count_trees(data, right, down):
    tree_count = 0
    for location in slope_location_generator(data, right, down):
        if location == "#":
            tree_count += 1
    return tree_count


def part_1(slope_map):
    print(f"Part 1: {count_trees(slope_map, 3, 1)}")


def part_2(slope_map):
    tree_encounters_per_slope = []
    for right, down in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
        tree_encounters_per_slope.append(count_trees(slope_map, right, down))

    score = 1
    for trees in tree_encounters_per_slope:
        score *= trees

    print(f"Part 2: {score}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 207
    part_2(data)  # Correct answer: 2655892800