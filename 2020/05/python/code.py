from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def compute_row(s: str) -> int:
    rows = [i for i in range(128)]

    for char in s:
        if char == "F":
            rows = rows[0 : len(rows) // 2]
        else:
            rows = rows[len(rows) // 2 :]

    return rows[0]


def compute_col(s:str) -> int:
    cols = [i for i in range(8)]

    for char in s:
        if char == "L":
            cols = cols[0 : len(cols) // 2]
        else:
            cols = cols[len(cols) // 2 :]

    return cols[0]


def both_parts(data):
    seat_ids = []
    highest_seat_id = 0
    row_of_highest = -1
    col_of_highest = -1

    for bsp in data:
        row = compute_row(bsp[0:8])
        col = compute_col(bsp[7:])
        seat_id = row * 8 + col
        seat_ids.append(seat_id)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
            row_of_highest = row
            col_of_highest = col

    print(f"Part 1: Row: {row_of_highest} | Col: {col_of_highest} | Seat ID: {row_of_highest * 8 + col_of_highest}")

    seat_ids.sort()
    for i in range(seat_ids[0], seat_ids[-1]):
        if i not in seat_ids:
            print(f"Part 2: My seat ID is {i}")
            break


if __name__ == "__main__":
    data = read_input()
    # Correct answer: 915
    # Correct answer: 699
    both_parts(data)