import json
from itertools import zip_longest
from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def packet_compare(left_item, right_item):
    r_val = "equal"
    for left, right in zip_longest(left_item, right_item):
        if left is None:
            r_val = True
            # print(f"left is None : {r_val}")
            break
        elif right is None:
            r_val = False
            # print(f"right is None : {r_val}")
            break
        elif isinstance(left, list) and isinstance(right, list):
            # print("both are lists, drilling down")
            r_val = packet_compare(left, right)
            if r_val != "equal":
                break
        elif isinstance(left, list) and not isinstance(right, list):
            # print("left == list; right != list")
            r_val = packet_compare(left, [right])
            if r_val != "equal":
                break
        elif not isinstance(left, list) and isinstance(right, list):
            # print("left != list; right == list")
            r_val = packet_compare([left], right)
            if r_val != "equal":
                break
        elif left > right:
            r_val = False
            # print(f"left > right : {left} > {right} : {r_val}")
            break
        elif left < right:
            r_val = True
            # print(f"right > left : {right} > {left} : {r_val}")
            break
        else:
            # print(f"equal : {left} = {right} : pass")
            pass
    return r_val


def part_1(data):
    idx = 1
    right_order = []
    for pair in data.split("\n\n"):
        # print(idx)
        raw_left, raw_right = pair.split()
        left_packet = json.loads(raw_left)
        right_packet = json.loads(raw_right)

        if packet_compare(left_packet, right_packet):
            right_order.append(idx)

        idx += 1
        # print()
    # print(right_order)
    print(f"Part 1: {sum(right_order)}")


def part_2(data):
    packets_less_than_2 = 1
    packets_less_than_6 = 2
    packet_2 = json.loads("[[2]]")
    packet_6 = json.loads("[[6]]")

    no_empty_spaces = data.replace("\n\n", "\n")
    data_list = no_empty_spaces.split()

    for raw_packet in data_list:
        packet = json.loads(raw_packet.strip())

        if packet_compare(packet, packet_2):
            packets_less_than_2 += 1

        if packet_compare(packet, packet_6):
            packets_less_than_6 += 1

    # print("index of packet [[2]] =", packets_less_than_2)
    # print("index of packet [[6]] =", packets_less_than_6)
    print(f"Part 2: {packets_less_than_2 * packets_less_than_6}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 5503
    part_2(data)  # Correct answer: 20952