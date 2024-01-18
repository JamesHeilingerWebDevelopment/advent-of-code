from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        file_input = fp.read()
        return file_input.split("\n")


def make_color_dict(color_string):
    color_dict = {"red": 0, "green": 0, "blue": 0}

    for color_count in color_string.split(", "):
        number, color = color_count.split()
        if color == "red":
            color_dict["red"] = int(number)
        elif color == "green":
            color_dict["green"] = int(number)
        else:
            color_dict["blue"] = int(number)

    return color_dict


def part_1(data):
    red, green, blue, total = 12, 13, 14, 0

    for line in data:
        tag, all_groups = line.split(": ")
        groups = all_groups.split("; ")
        scoreboard = []
        for group in groups:
            color_dict = make_color_dict(group)
            if color_dict["red"] <= red and color_dict["green"] <= green and color_dict["blue"] <= blue:
                scoreboard.append(True)
            else:
                scoreboard.append(False)
        if all(scoreboard):
            total += int(tag.split()[1])

    print(f"Part 1: {total}")


def part_2(data):
    total = 0
    for line in data:
        red, green, blue = 0, 0, 0
        _, all_groups = line.split(": ")
        groups = all_groups.split("; ")
        for group in groups:
            for color_count in group.split(", "):
                number, color = color_count.split()
                if color == "red" and int(number) > red:
                    red = int(number)
                elif color == "green" and int(number) > green:
                    green = int(number)
                elif color == "blue" and int(number) > blue:
                    blue = int(number)

        total += red * green * blue
    print(f"Part 2: {total}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 2237
    part_2(data)  # Correct answer: 66681