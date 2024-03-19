from collections import namedtuple
from functools import wraps
from operator import itemgetter
from sys import argv
from time import perf_counter


SECANT = 2000000


Point = namedtuple("Point", ["x", "y"])


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        time_end = perf_counter()
        print(f"{func.__name__}: {result} | Execution time: {time_end - time_start}")
        return result
    return wrapper


def manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def process_input_generator(data: list[str]):
    for s in data:
        sensor = Point(int(s.split(":")[0].split(",")[0].split("=")[1]), int(s.split(":")[0].split(",")[1].split("=")[1]))
        beacon = Point(int(s.split(":")[1].split(",")[0].split("=")[1]), int(s.split(":")[1].split(",")[1].split("=")[1]))
        yield sensor, manhattan_distance(sensor, beacon)


def manhattan_circle_secant_intersection(center: Point, radius: int, secant: int) -> tuple[int | None, int | None]:
    # Compute inersection of the secant
    max_width = radius * 2 + 1
    vertical_offset = abs(center.y - secant)
    secant_intersection = max_width - (vertical_offset * 2)
    if secant_intersection <= 0:
        return None, None

    # Get max and min x values of the secant through the manhattan circle
    half_secant_width = secant_intersection // 2
    max_x = center.x + half_secant_width
    min_x = center.x - half_secant_width
    return min_x, max_x


@execution_time
def part_1(data):
    intersections = []

    for point, radius in process_input_generator(data):
        current_intersection = manhattan_circle_secant_intersection(point, radius, SECANT)
        if current_intersection[0] is not None:
            intersections.append(current_intersection)

    return max(intersections, key=itemgetter(1))[1] - min(intersections)[0]


def collapse_ranges(ranges: list[tuple[int, int]]):
    """This works for my data but doesn't work on the example data.

    It needs to account for ranges that are adjacent to each other but not overlapping.
    """
    final_ranges = [ranges[0]]
    for range in ranges[1:]:

        if range[0] >= final_ranges[0][0] and range[1] <= final_ranges[0][1]:
            pass

        elif range[0] <= final_ranges[0][0] and range[1] >= final_ranges[0][1]:
            del final_ranges[0]
            final_ranges.append(range)

        elif range[0] <= final_ranges[0][0] and (range[1] <= final_ranges[0][1] and range[1] >= final_ranges[0][0]):
            temp_range = final_ranges.pop(0)
            final_ranges.append((range[0], temp_range[1]))

        elif (range[0] >= final_ranges[0][0] and range[0] <= final_ranges[0][1]) and range[1] >= final_ranges[0][1]:
            temp_range = final_ranges.pop(0)
            final_ranges.append((temp_range[0], range[1]))

        else:
            final_ranges.append(range)

    if len(final_ranges) == len(ranges):
        return final_ranges
    else:
        return collapse_ranges(final_ranges)


@execution_time
def part_2(data):
    SEARCH_LIMIT = 4000000

    for search_line in range(SEARCH_LIMIT, 0, -1):
        if search_line % 100000 == 0:
            print(search_line)

        intersections = []
        for point, radius in process_input_generator(data):
            current_intersection = manhattan_circle_secant_intersection(point, radius, search_line)
            if current_intersection[0] is not None:
                intersections.append(current_intersection)

        collapsed_ranges = collapse_ranges(sorted(intersections))
        if len(collapsed_ranges) > 1:
            y_coord = search_line
            break

    print(collapsed_ranges)

    print(f"{collapsed_ranges[0][1] + 1} * 4000000 + {y_coord} = {(collapsed_ranges[0][1] + 1) * 4000000 + y_coord}")
    return (collapsed_ranges[0][1] + 1) * 4000000 + y_coord


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 6275922
    part_2(data)  # Correct answer: 11747175442119
