from sys import argv


DEBUG = False


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def part_1(passports):
    valid_passports = 0
    rqd = ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"]
    split_passports = passports.split("\n\n")
    for psprt in split_passports:
        if (
            rqd[0] in psprt
            and rqd[1] in psprt
            and rqd[2] in psprt
            and rqd[3] in psprt
            and rqd[4] in psprt
            and rqd[5] in psprt
            and rqd[6] in psprt
        ):
            valid_passports += 1
    print(f"Part 1: {valid_passports}")


def part_2(passports):
    valid_passports = 0
    split_passports = passports.split("\n\n")
    for psprt in split_passports:
        p = {}
        for item in psprt.split():
            p[item.split(":")[0]] = item.split(":")[1]

        if validate_fields(p, DEBUG):
            valid_passports += 1
    print(f"Part 2: {valid_passports}")


def validate_fields(d: dict, debug: bool = False) -> bool:
    if (
        "byr" in d
        and "iyr" in d
        and "eyr" in d
        and "hgt" in d
        and "hcl" in d
        and "ecl" in d
        and "pid" in d
    ):
        return validate_byr(d, DEBUG)
    else:
        if debug:
            print(f"{d} failed field validation")
        return False


def validate_byr(d: dict, debug: bool = False) -> bool:
    try:
        if int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002:
            return validate_iyr(d, DEBUG)
        else:
            if debug:
                print(f"{d}: byr outside of range")
            return False
    except ValueError:
        if debug:
            print(f"{d}: byr is not an integer")
        return False


def validate_iyr(d: dict, debug: bool = False) -> bool:
    try:
        if int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020:
            return validate_eyr(d, DEBUG)
        else:
            if debug:
                print(f"{d}: iyr outside of range")
            return False
    except ValueError:
        if debug:
            print(f"{d}: iyr is not and integer")
        return False


def validate_eyr(d: dict, debug: bool = False) -> bool:
    try:
        if int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030:
            return validate_hcl(d, DEBUG)
        else:
            if debug:
                print(f"{d}: eyr is not and integer")
        return False
    except ValueError:
        if debug:
            print(f"{d}: eyr is not an integer")
        return False


def validate_hcl(d: dict, debug: bool = False) -> bool:
    if d["hcl"][0] == "#" and len(d["hcl"]) == 7:
        try:
            int(d["hcl"].strip("#"), 16)
            return validate_ecl(d, DEBUG)
        except ValueError:
            if debug:
                print(f"{d}: hcl is not an integer")
            return False
    else:
        if debug:
            print(f"{d}: hcl failed validation")
        return False


def validate_ecl(d: dict, debug: bool = False) -> bool:
    if d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return validate_pid(d, DEBUG)
    else:
        if debug:
            print(f"{d}: ecl failed validation")
        return False


def validate_pid(d: dict, debug: bool = False) -> bool:
    if len(d["pid"]) == 9:
        try:
            _ = int(d["pid"])
            return validate_hgt(d, DEBUG)
        except ValueError:
            if debug:
                print(f"{d}: pid is not an integer")
            return False
    else:
        if debug:
            print(f"{d}: pid is longer than 9 digits")
        return False


def validate_hgt(d: dict, debug: bool = False) -> bool:
    if d["hgt"][-2:] == "cm":
        try:
            if int(d["hgt"][:-2]) >= 150 and int(d["hgt"][:-2]) <= 193:
                return True
            else:
                if debug:
                    print(f"{d}: hgt centimeters outside of range")
                return False
        except ValueError:
            if debug:
                print(f"{d}: hgt centimeters is not a number")
            return False
    elif d["hgt"][-2:] == "in":
        try:
            if int(d["hgt"][:-2]) >= 59 and int(d["hgt"][:-2]) <= 76:
                return True
            else:
                if debug:
                    print(f"{d}: hgt inches outside of range")
                return False
        except ValueError:
            if debug:
                print(f"{d}: hgt inches is not a number")
            return False
    else:
        if debug:
            print(f'{d}: hgt does not contain "cm" or "in"')
        return False


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 210
    part_2(data)  # Correct answer: 131
