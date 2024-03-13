from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def dir_build(tree, trail, payload):
    if len(trail) > 1:
        dir_build(tree[trail[0]], trail[1:], payload)
    else:
        tree[trail[0]] = payload
        return


def dir_size(tree):
    size = 0
    for key, val in tree.items():
        try:
            size += val
        except TypeError:
            size += dir_size(tree[key])

    return size


def dir_walk(file_system: dict, total_disk_space: int, used_space: int, space_needed: int) -> tuple[int, list[int]]:
    sum_under_limit = 0
    large_directories = []
    for key in file_system:
        if isinstance(file_system[key], dict):
            size = dir_size(file_system[key])
            if size <= 100000:
                sum_under_limit += size
            total, dir_sizes = dir_walk(file_system[key], total_disk_space, used_space, space_needed)
            sum_under_limit += total
            large_directories.extend(dir_sizes)
            if size >= space_needed - total_disk_space + used_space:
                large_directories.append(size)
                # print(f"{key} = {size}")
    return sum_under_limit, large_directories


def part_1(data):
    dir_trail = []
    fs = {}
    for line in data:
        if "$ cd .." in line:
            dir_trail.pop(-1)
        elif "$ cd " in line:
            dir_trail.append(line.split("$ cd ")[1].strip())
            dir_build(fs, dir_trail, {})
        elif "$ ls" in line or "dir " in line:
            pass
        else:
            size, fname = line.split(" ")
            dir_trail.append(fname.strip())
            dir_build(fs, dir_trail, int(size))
            dir_trail.pop(-1)
    total, largest_dirs = dir_walk(fs, 70000000, dir_size(fs), 30000000)
    print(f"Part 1: {total}")
    return largest_dirs


def part_2(data):
    data.sort()
    print(f"Part 2: {data[0]}")


if __name__ == "__main__":
    # Part 1: 1490523
    # Part 2: 12390492
    part_2(part_1(read_input()))