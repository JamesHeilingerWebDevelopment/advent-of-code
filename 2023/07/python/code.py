from collections import namedtuple
from sys import argv
from time import time


RANKS = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}
Hand = namedtuple("Hand", "cards bid")


def read_input():
    with open(argv[1], "r") as fp:
        return [Hand(x.split()[0], int(x.split()[1])) for x in fp.read().split("\n")]


def classify_and_sort_hands(hands):
    order = "AKQJT98765432"
    hand_classification = {
        "5-of-a-kind": [],
        "4-of-a-kind": [],
        "full-house": [],
        "3-of-a-kind": [],
        "2-pair": [],
        "1-pair": [],
        "high-card": [],
    }
    for hand in hands:
        counted = [hand.cards.count(x) for x in RANKS.keys()]
        if 5 in counted:
            hand_classification["5-of-a-kind"].append(hand)
        elif 4 in counted:
            hand_classification["4-of-a-kind"].append(hand)
        elif 3 in counted and 2 in counted:
            hand_classification["full-house"].append(hand)
        elif 3 in counted:
            hand_classification["3-of-a-kind"].append(hand)
        elif counted.count(2) == 2:
            hand_classification["2-pair"].append(hand)
        elif counted.count(2) == 1:
            hand_classification["1-pair"].append(hand)
        else:
            hand_classification["high-card"].append(hand)

    for hand_type in hand_classification.values():
        hand_type.sort(key=lambda val: [order.index(c) for c in val.cards])

    return hand_classification


def compute_score(sorted_hands: dict, multiplier: int) -> int:
    score = 0
    for val in sorted_hands.values():
        for hand in val:
            score += hand.bid * multiplier
            multiplier -= 1
    return score


def part_1(hands):
    start_time = time()
    print(f"Part 1: {compute_score(classify_and_sort_hands(hands), len(hands))} | Execution time: {time() - start_time}")


def classify_and_sort_hands_joker_rules(hands):
    order = "AKQT98765432J"
    hand_classification = {
        "5-of-a-kind": [],
        "4-of-a-kind": [],
        "full-house": [],
        "3-of-a-kind": [],
        "2-pair": [],
        "1-pair": [],
        "high-card": [],
    }
    for hand in hands:
        counted = [hand.cards.count(x) for x in RANKS.keys() if x != "J"]
        jokers = hand.cards.count("J")

        # 5 of a kind with jokers
        if jokers == 5:
            hand_classification["5-of-a-kind"].append(hand)
        elif 4 in counted and jokers == 1:
            hand_classification["5-of-a-kind"].append(hand)
        elif 3 in counted and jokers == 2:
            hand_classification["5-of-a-kind"].append(hand)
        elif 2 in counted and jokers == 3:
            hand_classification["5-of-a-kind"].append(hand)
        elif 1 in counted and jokers == 4:
            hand_classification["5-of-a-kind"].append(hand)

        # 4 of a kind with jokers
        elif 3 in counted and jokers == 1:
            hand_classification["4-of-a-kind"].append(hand)
        elif 2 in counted and jokers == 2:
            hand_classification["4-of-a-kind"].append(hand)
        elif 1 in counted and jokers == 3:
            hand_classification["4-of-a-kind"].append(hand)

        # Full house with jokers
        elif counted.count(2) == 2 and jokers == 1:
            hand_classification["full-house"].append(hand)

        # 3 of a kind with jokers
        elif 2 in counted and jokers == 1:
            hand_classification["3-of-a-kind"].append(hand)
        elif 1 in counted and jokers == 2:
            hand_classification["3-of-a-kind"].append(hand)

        # 1 pair with jokers
        elif 1 in counted and jokers == 1:
            hand_classification["1-pair"].append(hand)

        elif 5 in counted:
            hand_classification["5-of-a-kind"].append(hand)
        elif 4 in counted:
            hand_classification["4-of-a-kind"].append(hand)
        elif 3 in counted and 2 in counted:
            hand_classification["full-house"].append(hand)
        elif 3 in counted:
            hand_classification["3-of-a-kind"].append(hand)
        elif counted.count(2) == 2:
            hand_classification["2-pair"].append(hand)
        elif counted.count(2) == 1:
            hand_classification["1-pair"].append(hand)
        else:
            hand_classification["high-card"].append(hand)

    for hand_type in hand_classification.values():
        hand_type.sort(key=lambda val: [order.index(c) for c in val.cards])

    return hand_classification


def part_2(hands):
    start_time = time()
    print(f"Part 2: {compute_score(classify_and_sort_hands_joker_rules(hands), len(hands))} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 251121738
    part_2(data)  # Correct answer: 251421071