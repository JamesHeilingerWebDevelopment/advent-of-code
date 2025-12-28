from sys import argv


class Node:
    def __init__(self, number, right_node=None, left_node=None):
        self.counter = 0
        self.number = number
        self.left = left_node
        self.right = right_node

    def add_left_node(self, node):
        self.left = node

    def add_right_node(self, node):
        self.right = node

    def move_left(self):
        self.left.move_to()
        return self.left

    def move_right(self):
        self.right.move_to()
        return self.right

    def move_to(self):
        self.counter += 1


class Graph:
    def __init__(self, directions):
        self.directons = directions

        nodes = [Node(number=x) for x in range(0, 100)]

        self.node = nodes[50]
        self.zero_node = nodes[0]

        for node in nodes:
            idx = nodes.index(node)
            if idx == 0:
                node.add_left_node(nodes[len(nodes)-1])
                node.add_right_node(nodes[idx+1])
            elif idx == len(nodes) - 1:
                node.add_left_node(nodes[idx-1])
                node.add_right_node(nodes[0])
            else:
                node.add_left_node(nodes[idx-1])
                node.add_right_node(nodes[idx+1])

    def left_steps(self, count):
        for _ in range(count):
            self.node = self.node.move_left()

    def right_steps(self, count):
        for _ in range(count):
            self.node = self.node.move_right()

    def follow_directions(self):
        for step in self.directons:
            if step[0] == "L":
                self.left_steps(int(step[1:]))
            else:
                self.right_steps(int(step[1:]))



def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    # dial = [x for x in range(0, 100)]
    pointer = 50
    counter = 0

    for item in data:
        if item[0] == "L":
            pointer -= int(item[1:])
        else:
            pointer += int(item[1:])

        if pointer >= 100 or pointer < 0:
            pointer %= 100

        if pointer == 0:
            counter += 1

    print(f"Part 1: {counter}")


def part_2(data):
    lock = Graph(data)
    lock.follow_directions()

    print(f"Part 2: {lock.zero_node.counter}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 989
    part_2(data)  # Correct answer: 5941 is too high