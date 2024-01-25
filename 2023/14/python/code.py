from sys import argv
from time import time


class Platform:
    def __init__(self, data_file: str) -> None:
        self.platform = self._read_input(data_file)
        self.total_load = 0

    def tilt_north(self) -> None:
        self._rotate_270()
        self._slide()
        self._rotate_90()

    def tilt_south(self) -> None:
        self._rotate_90()
        self._slide()
        self._rotate_270()

    def tilt_east(self) -> None:
        self._rotate_180()
        self._slide()
        self._rotate_180()

    def tilt_west(self) -> None:
        self._slide()

    def spin_cycle(self) -> None:
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    def display_platform(self) -> None:
        for i in self.platform:
            print("".join(i))
        print()

    def compute_total_load_on_north_support_beams(self) -> int:
        total = 0
        self._rotate_180()
        for idx, row in enumerate(self.platform, 1):
            total += idx * row.count("O")
        self._rotate_180()
        self.total_load = total
        return total

    def _read_input(self, filename):
        with open(filename, "r") as fp:
            data = fp.read().split("\n")
        return [[y for y in x] for x in data]

    def _rotate_90(self) -> None:
        self.platform = [list(j) for j in zip(*self.platform[::-1])]

    def _rotate_180(self) -> None:
        self.platform = [list(j) for j in zip(*[list(j) for j in zip(*self.platform[::-1])][::-1])]

    def _rotate_270(self) -> None:
        self.platform = [list(j) for j in zip(*[list(j) for j in zip(*[list(j) for j in zip(*self.platform[::-1])][::-1])][::-1])]

    def _slide(self) -> None:
        slid_graph = []
        for line in self.platform:
            slid_graph.append(self._slide_line(line))
        self.platform = slid_graph

    def _slide_line(self, line: list) -> list:
        new_line = [x for x in line]
        for x in range(0, len(new_line)):
            if x != 0 and new_line[x] == "O" and new_line[x-1] == ".":
                new_line[x-1] = "O"
                new_line[x] = "."
        if new_line != line:
            return self._slide_line(new_line)
        else:
            return new_line


def part_1(platform: Platform):
    start_time = time()
    platform.display_platform()
    platform.tilt_north()
    print(platform.total_load)
    print(f"Part 1: {platform.compute_total_load_on_north_support_beams()} | Execution time: {time() - start_time}")


def part_2(platform: Platform):
    start_time = time()
    loads = []

    for _ in range(200):
        platform.spin_cycle()
        loads.append(platform.compute_total_load_on_north_support_beams())

    # Need to get these from some sort of cycle detector
    cycle_start = 107
    cycle_length = 42

    ending_value = 1000000000

    print(f"Part 2: {loads[((ending_value - cycle_start) % cycle_length) + cycle_start - 1]} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    platform = Platform(argv[1])
    part_1(platform)  # Correct answer: 105249
    part_2(platform)  # Correct answer: 88680