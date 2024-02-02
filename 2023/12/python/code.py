"""
This took me days, no, weeks to figure out. It was hard enough to get a recursive solution that worked,
but even harder for me to get a recursive solution that could be used with Dynamic Programming/Memoization.

I never looked at code solutions, but I did read many hints on the subreddit.
In the end, I wrote all the code myself (for the recursive solution, for the brute force I got the `lexico_permute_strings()` function from Stack Overflow).

Before I finally got the correct solution for part 2, I had 779 lines of code written (plus more before that that I had deleted, I'm sure).
If I were to discard the brute force method and use only the recursive solution, it would be 85 lines.
I like keeping the first solution I have around, to remind myself that the best solution was not what I first came up with.
"""
import functools
from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def lexico_permute_strings(s):
    """
    Generate all permutations in lexicographic order of string `s`.

    This algorithm, due to Narayana Pandita, is from 
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

    To produce the next permutation in lexicographic order of sequence `a`:

    1. Find the largest index j such that a[j] < a[j + 1]. If no such index exists,
    the permutation is the last permutation.
    2. Find the largest index k greater than j such that a[j] < a[k].
    3. Swap the value of a[j] with that of a[k].
    4. Reverse the sequence from a[j + 1] up to and including the final element a[n].

    Found at https://stackoverflow.com/a/43014919
    """
    a = sorted(s)
    n = len(a) - 1
    while True:
        yield "".join(a)

        # 1. Find the largest index j such that a[j] < a[j + 1]
        for j in range(n-1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return

        # 2. Find the largest index k greater than j such that a[j] < a[k]
        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break

        # 3. Swap the value of a[j] with that of a[k]
        a[j], a[k] = a[k], a[j]

        # Reverse the tail of the sequence
        a[j+1:] = a[j+1:][::-1]


def create_test_strings(record: str, backup: str) -> list[str]:
    test_strings = []

    total_broken = sum([int(x) for x in backup.split(",")]) - record.count("#")
    temp_string = "#" * total_broken + "." * (record.count("?") - total_broken)
    idxs = [i for i, j in enumerate(record) if j == "?"]
    perms = lexico_permute_strings(temp_string)

    temp_list = [x for x in record]
    for char in perms:
        for y, z in zip(idxs, char):
            temp_list[y] = z
        test_strings.append("".join(temp_list))
    return test_strings


def test_against_pattern(strings: list[str], pattern: str):
    count = 0
    correct_pattern = [int(x) for x in pattern.split(",")]

    for s in strings:
        test = [x.count("#") for x in s.split(".") if x != ""]
        if test == correct_pattern:
            count += 1

    return count


@functools.cache
def recursive_solution(springs: str, backup: str, hash_count: int) -> int:
    total = 0
    backup_list = backup.split(",")

    if len(springs) == 0 and len(backup) == 0:
        if hash_count == 0:
            return 1
        else:
            return 0
    elif len(springs) == 0 and len(backup_list) == 1 and hash_count == int(backup_list[0]):
        return 1
    elif len(backup) == 0 and hash_count > 0:
        return 0
    elif len(backup) > 0 and hash_count > int(backup_list[0]):
        return 0
    elif len(springs) == 0 and len(backup) > 0:
        return 0
    elif springs[0] == "#" and len(backup) == 0:
        return 0
    elif hash_count > 0 and springs[0] == "." and hash_count < int(backup[0]):
        return 0
    elif springs[0] == "#":
        total += recursive_solution(springs[1:], backup, hash_count + 1)
    elif springs[0] == ".":
        if hash_count > 0:
            if hash_count < int(backup_list[0]):
                return 0
            total += recursive_solution(springs[1:], ",".join(backup_list[1:]), 0)
        else:
            total += recursive_solution(springs[1:], backup, 0)
    else:
        # Try it as if it was a "."
        if hash_count > 0:
            if hash_count >= int(backup_list[0]):
                total += recursive_solution(springs[1:], ",".join(backup_list[1:]), 0)
        else:
            total += recursive_solution(springs[1:], backup, 0)

        # Try is as if it was a "#"
        total += recursive_solution(springs[1:], backup, hash_count + 1)

    return total


def part_1(data):
    print("***** Direct Solution *****")
    start_time = time()
    total = 0
    for line in data:
        record, backup = line.split()
        total += test_against_pattern(create_test_strings(record, backup), backup)
    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def part_1_recursive_solution(data):
    print("\n ***** Recursive Solution *****")
    start_time = time()
    total = 0
    for line in data:
        record, backup = line.split()
        total += recursive_solution(record, backup, 0)
    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def part_2(data):
    start_time = time()
    total = 0
    for line in data:
        record, backup = line.split()
        expanded_record = "?".join([record for _ in range(5)])
        expanded_backup = ",".join([backup for _ in range(5)])
        total += recursive_solution(expanded_record, expanded_backup, 0)
    print(f"Part 2: {total} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()

    part_1(data)  # Correct answer: 7653

    part_1_recursive_solution(data)
    part_2(data)  # Correct answer: 60681419004564