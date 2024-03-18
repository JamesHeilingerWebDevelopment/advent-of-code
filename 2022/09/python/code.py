from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def get_limits(data, display=False):
    vertical = [0]
    horizontal = [0]

    for line in data:
        direction = line.strip().split()[0]
        amount = int(line.strip().split()[1])

        if direction == "U":
            vertical.append(vertical[-1] + amount)
        elif direction == "D":
            vertical.append(vertical[-1] - amount)
        elif direction == "R":
            horizontal.append(horizontal[-1] + amount)
        else:
            horizontal.append(horizontal[-1] - amount)

    return max(horizontal), min(horizontal), max(vertical), min(vertical)


def create_graph(limits):
    x_max, x_min, y_max, y_min = limits
    x_axis = abs(x_max) + abs(x_min) + 2
    y_axis = abs(y_max) + abs(y_min) + 2

    return [[" " for _ in range(x_axis)] for _ in range(y_axis)], (abs(x_min), abs(y_min),)


def add_to_graph(graph, x, y, char="#"):
    graph[y][x] = char
    return graph


def head_and_tail_are_touching(hx, hy, tx, ty):
    if (hx == tx) and (hy == ty):
        # The head and tail are on top of each other, they are touching
        return True
    elif abs(abs(hx) - abs(tx)) <= 1 and abs(abs(hy) - abs(ty)) <= 1:
        return True
    else:
        return False


def update_tail(hx, hy, tx, ty):
    # This hols the logic of how to move the tail based on the new head position.
    if not head_and_tail_are_touching(hx, hy, tx, ty):
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
        else:
            pass

        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
        else:
            pass

    return tx, ty


def write_output(fname, graph_data):
    with open(fname, "w") as of:
        for row in reversed(graph_data):
            of.write("".join(row))
            of.write("\n")


def part_1(data):
    start_time = time()
    graph, origin = create_graph(get_limits(data))

    head_x = origin[0]
    head_y = origin[1]
    tail_x = origin[0]
    tail_y = origin[1]

    for line in data:
        direction = line.strip().split()[0]
        amount = int(line.strip().split()[1])

        for i in range(amount):
            if direction == "U":
                head_y += 1
            elif direction == "D":
                head_y -= 1
            elif direction == "R":
                head_x += 1
            else:
                head_x -= 1

            tail_x, tail_y = update_tail(head_x, head_y, tail_x, tail_y)
            graph = add_to_graph(graph, tail_x, tail_y)

    write_output("output_part_1.txt", graph)
    visit_count = 0
    for row in graph:
        visit_count += row.count("#")
    print(f"Part 1: {visit_count} | Execution time: {time() - start_time}")


def part_2(data):
    start_time = time()
    graph, origin = create_graph(get_limits(data))

    rope = [[origin[0], origin[1]] for _ in range(10)]

    for line in data:
        direction = line.strip().split()[0]
        amount = int(line.strip().split()[1])

        for i in range(amount):
            if direction == "U":
                rope[0][1] += 1
            elif direction == "D":
                rope[0][1] -= 1
            elif direction == "R":
                rope[0][0] += 1
            else:
                rope[0][0] -= 1

            for knot in range(1,10):
                rope[knot][0], rope[knot][1] = update_tail(
                    rope[knot-1][0], rope[knot-1][1], rope[knot][0], rope[knot][1]
                )

            graph = add_to_graph(graph, rope[9][0], rope[9][1])

    write_output("output_part_2.txt", graph)
    visit_count = 0
    for row in graph:
        visit_count += row.count("#")

    print(f"Part 2: {visit_count} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 6197
    part_2(data)  # Correct answer: 2562