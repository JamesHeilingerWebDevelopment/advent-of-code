from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    visible_trees = 0
    rows = []
    cols = []
    for line in data:
        rows.append([int(x) for x in line.strip()])
    for i in range(len(line.strip())):
        col = []
        for row in rows:
            col.append(row[i])
        cols.append(col)

    for col_idx in range(len(cols[0])):
        for row_idx in range(len(rows[0])):
            if col_idx == 0 or row_idx == 0 or col_idx == len(cols[:-1]) or row_idx == len(rows[:-1]):
                # This checks for trees on the outside edge
                visible_trees += 1
            else:
                height = cols[col_idx][row_idx]
                west = rows[row_idx][0:col_idx]
                east = rows[row_idx][col_idx+1:]
                north = cols[col_idx][0:row_idx]
                south = cols[col_idx][row_idx+1:]
                if (max(west) < height) or (max(east) < height) or (max(north) < height) or (max(south) < height):
                    visible_trees += 1

    print(f"Part 1: {visible_trees}")


def part_2(data):
    view_scores = []
    rows = []
    cols = []
    for line in data:
        rows.append([int(x) for x in line.strip()])
    for i in range(len(line.strip())):
        col = []
        for row in rows:
            col.append(row[i])
        cols.append(col)

    for col_idx in range(len(cols[0])):
        for row_idx in range(len(rows[0])):
            west_score = 0
            east_score = 0
            north_score = 0
            south_score = 0

            height = cols[col_idx][row_idx]

            west = rows[row_idx][0:col_idx]
            west.reverse()
            east = rows[row_idx][col_idx+1:]
            north = cols[col_idx][0:row_idx]
            north.reverse()
            south = cols[col_idx][row_idx+1:]

            for tree in west:
                if tree >= height:
                    west_score += 1
                    break
                else:
                    west_score += 1

            for tree in east:
                if tree >= height:
                    east_score += 1
                    break
                else:
                    east_score += 1

            for tree in north:
                if tree >= height:
                    north_score += 1
                    break
                else:
                    north_score += 1

            for tree in south:
                if tree >= height:
                    south_score += 1
                    break
                else:
                    south_score += 1

            view_score = west_score * east_score * north_score * south_score
            view_scores.append(view_score)

    print(f"Part 2: {max(view_scores)}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 1798
    part_2(data)  # Correct answer: 259308