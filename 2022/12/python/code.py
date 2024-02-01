from functools import wraps
from queue import Queue
from sys import argv
from time import perf_counter


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {result} | Execution time: {perf_counter() - time_start}")
        return result
    return wrapper


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def make_adjacency_list(graph: list[list[str]]) -> list[list[int]]:
    adj_list = []
    y_offset = len(graph[0])
    idx = -1

    for y in range(len(graph)):
        for x in range(len(graph[y])):
            idx += 1
            temp_edge_list = []

            # Checking to the north
            if y > 0 and ord(graph[y-1][x]) - ord(graph[y][x]) <= 1:
                temp_edge_list.append(idx - y_offset)

            # Checking to the south
            if y < len(graph) - 1 and ord(graph[y+1][x]) - ord(graph[y][x]) <= 1:
                temp_edge_list.append(idx + y_offset)

            # Checking to the east
            if x < len(graph[0]) - 1 and ord(graph[y][x+1]) - ord(graph[y][x]) <= 1:
                temp_edge_list.append(idx + 1)

            # Checking to the west
            if x > 0 and ord(graph[y][x-1]) - ord(graph[y][x]) <= 1:
                temp_edge_list.append(idx - 1)

            adj_list.append(temp_edge_list)

    return adj_list


def make_graph(data: list[str]) -> list[list[str]]:
    raw_graph = []
    for line in data:
        raw_graph.append([x for x in line])
    return raw_graph


def get_start_node(graph: list[str]) -> int:
    return "".join(graph).find("`")


def traverse_graph(adj_list: list[list[int]], starting_node: int, ending_node: int) -> int:
    q = Queue()
    q.put(starting_node)
    distance = -1
    start_flag = True
    graph = [{"pred": None, "dist": None} for _ in adj_list]

    # Update the starting node in the graph
    graph[starting_node]["dist"] = 0

    while not q.empty():
        distance += 1
        node = q.get()

        if graph[node]["dist"] == None and not start_flag:
            graph[node]["dist"] = graph[graph[node]["pred"]]["dist"] + 1

        start_flag = False
        for x in adj_list[node]:
            if graph[x]["pred"] == None:
                graph[x]["pred"] = node
                q.put(x)

    return graph[ending_node]["dist"]


@execution_time
def part_1(data):
    return traverse_graph(make_adjacency_list(make_graph(data)), "".join(data).find("`"), "".join(data).find("{"))


def starting_node_generator(input_map: list[str]) -> int:
    flattened_input_map = "".join(input_map)
    count = 0
    for node in flattened_input_map:
        if node == "a":
            yield count
        count += 1


@execution_time
def part_2(data):
    shortest = 1000  # TODO: Get rid of this magic number!
    adjacency_list = make_adjacency_list(make_graph(data))
    end_node = "".join(data).find("{")
    for start_node in starting_node_generator(data):
        path_length = traverse_graph(adjacency_list, start_node, end_node)
        if path_length is not None and path_length < shortest:
            shortest = path_length
    return shortest


if __name__ == "__main__":
    raw_data = read_input()
    part_1(raw_data.replace("S", "`").replace("E", "{").split())  # Correct answer: 408
    part_2(raw_data.replace("S", "a").replace("E", "{").split())  # Correct answer: 399
