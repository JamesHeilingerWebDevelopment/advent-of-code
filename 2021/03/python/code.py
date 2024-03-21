from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    gamma_rate = ""
    epsilon_rate = ""

    for x in range(len(data[0].strip())):
        temp = []
        for binary_number in data:
            temp.append(binary_number[x])
        one_count = temp.count("1")
        if one_count > len(temp) / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    print("gamma_rate =", int(gamma_rate, 2))
    print("epsilon_rate =", int(epsilon_rate, 2))

    print(f"Part 1: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


def get_most_common_bit_at_index(data, idx):
    temp = []
    for binary_number in data:
        temp.append(binary_number[idx])

    bit_count = temp.count("1")
    if bit_count >= len(data) / 2:
        return 1
    else:
        return 0


def get_least_common_bit_at_index(data, idx):
    temp = []
    for binary_number in data:
        temp.append(binary_number[idx])

    bit_count = temp.count("1")
    if bit_count >= len(data) /2:
        return 0
    else:
        return 1


def filter_data_by_criteria(data, idx, most_common):
    if most_common == True:
        val = get_most_common_bit_at_index(data, idx)
    else:
        val = get_least_common_bit_at_index(data, idx)
    filtered_data = []
    for line in data:
        if int(line[idx]) == val:
            filtered_data.append(line)

    final_val = filtered_data
    if len(filtered_data) > 1:
        final_val = filter_data_by_criteria(filtered_data, idx + 1, most_common)
    return final_val


def compute_o2_gen_rating(dataset):
    return filter_data_by_criteria(dataset, 0, True)


def compute_co2_scrubber_rating(dataset):
    return filter_data_by_criteria(dataset, 0, False)


def part_2(data):
    o2_gen_rating = compute_o2_gen_rating(data)[0].strip()
    co2_scrubber_rating = compute_co2_scrubber_rating(data)[0].strip()

    print("O2 Generator Rating =", int(o2_gen_rating, 2))
    print("CO2 Scrubber Rating =", int(co2_scrubber_rating, 2))

    print(f"Part 2: {int(o2_gen_rating, 2) * int(co2_scrubber_rating, 2)}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 
    part_2(data)  # Correct answer: 