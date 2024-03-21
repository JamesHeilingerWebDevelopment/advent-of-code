from dataclasses import dataclass
from sys import argv


@dataclass
class Square:
    val: int
    marked: bool


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def get_call_numbers(data):
    return [int(i) for i in data.split("\n\n")[0].split(",")]


def get_game_boards(data) -> list:
    raw_boards = data.split("\n\n")[1:]
    boards = []
    for raw_board in raw_boards:
        split_raw_board = raw_board.split("\n")
        b = []
        for line in split_raw_board:
            b.append([Square(int(i), False) for i in line.split()])
        boards.append(b)

    return boards


def part_1(data):
    call_numbers = get_call_numbers(data)
    game_boards = get_game_boards(data)
    break_flag = False
    winning_score = 0
    winning_number = 0

    for num in call_numbers:
        for board in game_boards:
            for row in board:
                for col in row:
                    if col.val == num:
                        col.marked = True
            if check_for_win(board):
                winning_score = compute_score(board)
                winning_number = num
                break_flag = True
                break
        if break_flag:
            break

    print(f"Part 1: {winning_score * winning_number}")


def check_for_win(b):
    for r in b:
        if r[0].marked and r[1].marked and r[2].marked and r[3].marked and r[4].marked:
            return True

    if (
        (
            b[0][0].marked
            and b[1][0].marked
            and b[2][0].marked
            and b[3][0].marked
            and b[4][0].marked
        )
        or (
            b[0][1].marked
            and b[1][1].marked
            and b[2][1].marked
            and b[3][1].marked
            and b[4][1].marked
        )
        or (
            b[0][2].marked
            and b[1][2].marked
            and b[2][2].marked
            and b[3][2].marked
            and b[4][2].marked
        )
        or (
            b[0][3].marked
            and b[1][3].marked
            and b[2][3].marked
            and b[3][3].marked
            and b[4][3].marked
        )
        or (
            b[0][4].marked
            and b[1][4].marked
            and b[2][4].marked
            and b[3][4].marked
            and b[4][4].marked
        )
    ):
        return True

    return False


def compute_score(b):
    score = 0

    for row in b:
        score += sum([s.val for s in row if s.marked is False])

    return score


def part_2(data):
    call_numbers = get_call_numbers(data)
    game_boards = get_game_boards(data)
    gb_copy = game_boards.copy()
    winning_boards = []
    break_flag = False
    losing_score = 0
    losing_number = 0

    # Find losing board
    for num in call_numbers:
        for board in gb_copy:
            for row in board:
                for col in row:
                    if col.val == num:
                        col.marked = True
            if check_for_win(board):
                if board in game_boards:
                    game_boards.remove(board)
                if len(game_boards) == 1:
                    break_flag = True
                    break
        if break_flag:
            break_flag = False
            break

    # Get losing board score
    for num in call_numbers:
        for row in game_boards[0]:
            for col in row:
                if col.val == num:
                    col.marked = True
            if check_for_win(game_boards[0]):
                losing_score = compute_score(game_boards[0])
                losing_number = num
                break_flag = True
                break
        if break_flag:
            break

    print(f"Part 2: {losing_score * losing_number}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 46920
    part_2(data)  # Correct answer: 12635