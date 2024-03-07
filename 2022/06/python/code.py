from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def packet_processor(length: int, data: str) -> int:
    output = 0
    for val in range(length, len(data)):
        start_of_packet_flag = True
        packet = data[val-length:val]
        for char in packet:
            if packet.count(char) >= 2:
                start_of_packet_flag = False
        if start_of_packet_flag:
            output = val
            break
    return output


def part_1(data):
    print(f"Part 1: {packet_processor(4, data)}")


def part_2(data):
    print(f"Part 2: {packet_processor(14, data)}")


if __name__ == "__main__":
    part_1(read_input())  # Correct answer: 1702
    part_2(read_input())  # Correct answer: 3559