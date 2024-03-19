from sys import argv
from time import time


class RegolithReservoirBase:
    def __init__(self) -> None:
        self.scan = self.read_input()
        self.output_file = "output.txt"
        self.cave = [[]]
        self.part = "0"
        self.make_cave()
        self.sand_x = 0
        self.sand_y = 0
        self.stop_flag = False

    def make_cave(self):
        for line in self.scan:
            clean_split_line = line.strip().split(" -> ")
            first_pair_flag = True
            for pair in clean_split_line:
                if first_pair_flag:
                    x, y = pair.split(",")
                    x1 = int(x)
                    y1 = int(y)
                    first_pair_flag = False
                else:
                    x2 = x1
                    y2 = y1
                    x, y = pair.split(",")
                    x1 = int(x)
                    y1 = int(y)

                    self.make_rocks(x1, y1, x2, y2)

    def make_rocks(self, x1, y1, x2, y2):
        if y1 == y2:
            if x1 > x2:
                for i in range(x2, x1+1):
                    self.cave[y1][i] = "#"
            else:
                for i in range(x1, x2+1):
                    self.cave[y1][i] = "#"
        else:
            if y1 > y2:
                for j in range(y2, y1+1):
                    self.cave[j][x1] = "#"
            else:
                for j in range(y1, y2+1):
                    self.cave[j][x1] = "#"

    def write_output(self):
        with open(self.output_file, "w") as of:
            for layer in self.cave:
                of.write("".join(layer))
                of.write("\n")
        return

    def sand_slide(self):
        self.sand_falls()
        sand_units = 0
        for layer in self.cave:
            sand_units += layer.count("o")
        print(f"Part {self.part}: There are {sand_units} units of sand in the cave.")

    def sand_falls(self):
        while not self.stop_flag:
            self.sand_x = 500
            self.sand_y = 0
            self.check_down()

        self.write_output()

    def sand_stops(self):
        raise NotImplementedError

    def check_down(self):
        raise NotImplementedError

    def check_left(self):
        if self.cave[self.sand_y+1][self.sand_x-1] in ["#", "o"]:
            self.check_right()
        else:
            self.sand_x -= 1
            self.sand_y += 1
            self.check_down()

    def check_right(self):
        if self.cave[self.sand_y+1][self.sand_x+1] in ["#", "o"]:
            self.sand_stops()
        else:
            self.sand_x += 1
            self.sand_y += 1
            self.check_down()

    @staticmethod
    def read_input():
        with open(argv[1], "r") as fp:
            return fp.readlines()


class RegolithReservoir1(RegolithReservoirBase):
    def __init__(self) -> None:
        super().__init__()
        self.output_file = "output_part_1.txt"
        self.part = "1"

    def make_cave(self):
        self.cave = [[" " for _ in range(540)] for _ in range(173)]
        self.cave[0][500] = "+"

        return super().make_cave()

    def sand_stops(self):
        self.cave[self.sand_y][self.sand_x] = "o"

    def check_down(self):
        self.check_abyss()
        if self.stop_flag:
            pass
        elif self.cave[self.sand_y+1][self.sand_x] in ["#", "o"]:
            self.check_left()
        else:
            self.sand_y += 1
            self.check_down()

    def check_abyss(self):
        if self.sand_y+1 >= len(self.cave):
            self.stop_flag = True


class RegloithReservoir2(RegolithReservoirBase):
    def __init__(self) -> None:
        super().__init__()
        self.output_file = "output_part_2.txt"
        self.part = "2"

    def make_cave(self):
        self.cave = [[" " for _ in range(1000)] for _ in range(174)]
        self.cave[173] = ["#" for _ in range(1000)]
        self.cave[0][500] = "+"

        return super().make_cave()

    def sand_stops(self):
        self.cave[self.sand_y][self.sand_x] = "o"
        if self.sand_y == 0 and self.sand_x == 500:
            self.stop_flag = True

    def check_down(self):
        if self.cave[self.sand_y+1][self.sand_x] in ["#", "o"]:
            self.check_left()
        else:
            self.sand_y += 1
            self.check_down()


if __name__ == "__main__":
    rr1 = RegolithReservoir1()
    rr1.sand_slide()  # Correct answer: 1133
    rr2 = RegloithReservoir2()
    rr2.sand_slide()  # Correct answer: 27566