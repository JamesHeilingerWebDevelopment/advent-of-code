from collections import namedtuple
from sys import argv
from time import time


Lens = namedtuple("Lens", "label focal")


class LensBoxes:
    def __init__(self, number) -> None:
        self.boxes = {x:[] for x in range(number)}
        self.focusing_power = 0

    def dash_operator(self, box, label):
        idx = self.find_index_of_label(box, label)

        if idx != -1:
            del self.boxes[box][idx]

    def equal_operator(self, box, label, focal_length):
        idx = self.find_index_of_label(box, label)

        if idx == -1:
            self.boxes[box].append(Lens(label, int(focal_length)))
        else:
            self.boxes[box][idx] = Lens(label, int(focal_length))

    def find_index_of_label(self, box, label):
        val = -1
        for i in range(len(self.boxes[box])):
            if self.boxes[box][i].label == label:
                val = i
                break
        return val
    
    def compute_focusing_power(self):
        # One plus the box number of the lens in question.
        # The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
        # The focal length of the lens.
        for box in self.boxes:
            for slot_number in range(len(self.boxes[box])):
                focusing_power = box + 1
                focusing_power *= slot_number + 1
                focusing_power *= self.boxes[box][slot_number].focal
                self.focusing_power += focusing_power


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def hash(step: str) -> int:
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


def part_1(data):
    start_time = time()

    total = 0
    for step in data.split(","):
        total += hash(step)

    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def get_label(step: str) -> str:
    label = ""
    for char in step:
        if char not in ["=", "-"]:
            label += char
        else:
            break
    return label


def part_2(data):
    start_time = time()

    boxes = LensBoxes(256)

    for step in data.split(","):
        label = get_label(step)
        box = hash(label)
        try:
            # Equal operator
            focal_length = step.split("=")[1]
            boxes.equal_operator(box, label, focal_length)
        except IndexError:
            # Dash operator
            boxes.dash_operator(box, label)

    boxes.compute_focusing_power()

    print(f"Part 2: {boxes.focusing_power} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 509167
    part_2(data)  # Correct answer: 259333