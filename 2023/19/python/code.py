from sys import argv
from time import time
from typing import NamedTuple


Range = NamedTuple("Range", [("range_start", int), ("range_end", int)])
Workflow = NamedTuple("Rule", [("rating", str), ("operator", str), ("split_val", int), ("destination", str)])


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n\n")


def parse_input(rules, parts):
    cleaned_up_rules = {}
    for raw_rule in rules.split("\n"):
        rule_id, raw_r = raw_rule.strip("}").split("{")
        cleaned_up_rules[rule_id] = raw_r.split(",")

    cleaned_up_parts = []
    for raw_part in parts.split("\n"):
        raw_x, raw_m, raw_a, raw_s = raw_part.strip("{}").split(",")
        cleaned_up_parts.append(
            {
                "x": int(raw_x.split("=")[1]),
                "m": int(raw_m.split("=")[1]),
                "a": int(raw_a.split("=")[1]),
                "s": int(raw_s.split("=")[1]),
            }
        )
    return cleaned_up_rules, cleaned_up_parts


def parse_input_2(rules: str) -> dict:
    cleaned_up_rules = {}
    for raw_rule in rules.split("\n"):
        rule_id, raw_r = raw_rule.strip("}").split("{")
        node_rules = []
        for item in raw_r.split(",")[:-1]:
            node_rules.append(
                Workflow(
                    rating=item.replace("<", ">").split(">")[0],
                    operator=item[1],
                    split_val=int(
                        item.replace("<", ">").replace(":", ">").split(">")[1]
                    ),
                    destination=item.split(":")[1],
                )
            )
        node_rules.append(
            Workflow(
                rating="default",
                operator="=",
                split_val=-1,
                destination=raw_r.split(",")[-1],
            )
        )
        cleaned_up_rules[rule_id] = node_rules
    return cleaned_up_rules


def classify_part(part: dict, rule: str, rules: dict) -> bool:
    """Check the part characteristics against the rules.

    Args:
        part (dict): The part to check.
        rule (str): The current rule to check.
        rules (dict): The rules to check that part against.

    Returns:
        bool: True = Accepted, False = Rejected
    """
    for r in rules[rule]:
        if "<" in r:
            category, remainder = r.split("<")
            val_str, route = remainder.split(":")
            val = int(val_str)
            if part[category] < val:
                if route == "A":
                    return True
                elif route == "R":
                    return False
                else:
                    return classify_part(part, route, rules)
        elif ">" in r:
            category, remainder = r.split(">")
            val_str, route = remainder.split(":")
            val = int(val_str)
            if part[category] > val:
                if route == "A":
                    return True
                elif route == "R":
                    return False
                else:
                    return classify_part(part, route, rules)
        else:
            if r == "A":
                return True
            elif r == "R":
                return False
            else:
                return classify_part(part, r, rules)


def part_1(rules, parts):
    start_time = time()
    accepted_parts = []
    for part in parts:
        if classify_part(part, "in", rules):
            accepted_parts.append(part)

    total = 0
    for part in accepted_parts:
        total += part["x"] + part["m"] + part["a"] + part["s"]

    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def split_range(attribute: str, op: str, val: int, ranges: dict) -> tuple[dict, dict]:
    true_ranges = {
        "x": ranges["x"],
        "m": ranges["m"],
        "a": ranges["a"],
        "s": ranges["s"],
    }
    false_ranges = {
        "x": ranges["x"],
        "m": ranges["m"],
        "a": ranges["a"],
        "s": ranges["s"],
    }

    if op == ">":
        true_ranges[attribute] = Range(val + 1, ranges[attribute].range_end)
        false_ranges[attribute] = Range(ranges[attribute].range_start, val + 1)
    else:
        true_ranges[attribute] = Range(ranges[attribute].range_start, val)
        false_ranges[attribute] = Range(val, ranges[attribute].range_end)
    return true_ranges, false_ranges


def evaluate_workflow(workflow_id: str, rating_range: dict, workflow_map: dict[str, list[Workflow]]) -> list[dict[str, Range]]:
    accepted_ranges = []

    for workflow in workflow_map[workflow_id]:
        if workflow.rating == "default":
            if workflow.destination == "R":
                pass
            elif workflow.destination == "A":
                accepted_ranges.append(rating_range)
            elif workflow.rating == "default":
                accepted_ranges.extend(
                    evaluate_workflow(workflow.destination, rating_range, workflow_map)
                )
        else:
            range_true, rating_range = split_range(workflow.rating, workflow.operator, workflow.split_val, rating_range)

            if workflow.destination == "R":
                pass
            elif workflow.destination == "A":
                accepted_ranges.append(range_true)
            else:
                accepted_ranges.extend(evaluate_workflow(workflow.destination, range_true, workflow_map))

    return accepted_ranges


def compute_possibilities(r: dict[str, Range]) -> int:
    return (
        (r["x"].range_end - r["x"].range_start)
        * (r["m"].range_end - r["m"].range_start)
        * (r["a"].range_end - r["a"].range_start)
        * (r["s"].range_end - r["s"].range_start)
    )


def sum_ranges(ranges: list[dict[str, Range]]) -> int:
    list_of_individual_ranges = [compute_possibilities(x) for x in ranges]
    summed_ranges = sum(list_of_individual_ranges)
    return summed_ranges


def part_2(rules):
    start_time = time()
    print(f"Part 2: {sum_ranges(evaluate_workflow('in', {'x': Range(1, 4001), 'm': Range(1, 4001), 'a': Range(1, 4001), 's': Range(1, 4001)}, parse_input_2(rules)))} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    clean_data = parse_input(*data)
    part_1(*clean_data)  # Correct answer: 432788
    part_2(data[0])  # Correct answer: 142863718918201