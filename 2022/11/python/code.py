from sys import argv
from time import time


INSPECTION_LIST = [lambda x: x * 7, lambda x: x + 5, lambda x: x * x, lambda x: x + 6, lambda x: x * 11, lambda x: x + 8, lambda x: x + 1, lambda x: x + 4]


def test_worry_level(item, m , divisor, if_true, if_false):
    if item % divisor == 0:
        m[if_true]["items"].append(item)
    else:
        m[if_false]["items"].append(item)


def make_monkeys():
    monkeys = []

    with open(argv[1], "r") as fp:
        monkey_data = fp.read().split("\n\n")

    for idx, raw_monkey_data in enumerate(monkey_data):
        line_split_data = raw_monkey_data.split("\n")
        monkeys.append(
            {
                "divisor": int(line_split_data[3].split()[-1].strip()),
                "inspection_count": 0,
                "items": [int(x) for x in line_split_data[1].split(": ")[1].split(", ")],
                "inspection": INSPECTION_LIST[idx],
                "if_true": int(line_split_data[4].split()[-1].strip()),
                "if_false": int(line_split_data[5].split()[-1].strip())
            }
        )

    return monkeys


def part_1():
    start_time = time()
    monkeys = make_monkeys()

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey["items"]:
                item = monkey["inspection"](item)
                item = item // 3
                test_worry_level(item, monkeys, monkey["divisor"], monkey["if_true"], monkey["if_false"])
                monkey["inspection_count"] += 1
            monkey["items"] = []

    inspection_counts = [m["inspection_count"] for m in monkeys]
    sorted_inspection_counts = sorted(inspection_counts, reverse=True)
    print(f"Part 1: {sorted_inspection_counts[0] * sorted_inspection_counts[1]} | Execution time: {time() - start_time}")


def part_2():
    start_time = time()
    monkeys = make_monkeys()

    mod_val = 1
    for monkey in monkeys:
        mod_val *= monkey["divisor"]

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey["items"]:
                item = monkey["inspection"](item)
                item = item % mod_val
                test_worry_level(item, monkeys, monkey["divisor"], monkey["if_true"], monkey["if_false"])
                monkey["inspection_count"] += 1
            monkey["items"] = []

    inspection_counts = [m["inspection_count"] for m in monkeys]
    sorted_inspection_counts = sorted(inspection_counts, reverse=True)
    print(f"Part 2: {sorted_inspection_counts[0] * sorted_inspection_counts[1]} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    part_1()  # Correct answer: 113232
    part_2()  # Correct answer: 29703395016