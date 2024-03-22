from collections import namedtuple
from sys import argv


Node = namedtuple("Node", ["id", "qty"])


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def make_graph(lines: list) -> tuple[list, dict]:
    count = 0
    node_color_map = {}
    for line in lines:
        l = line.strip("\n").split()
        node_color_map[count] = l[0] + l[1]
        node_color_map[l[0] + l[1]] = count
        count += 1

    graph = [[] for _ in range(count)]

    for line in lines:
        l = line.strip("\n").split()
        try:
            if l[5] + l[6] != "otherbags.":
                graph[node_color_map[l[0] + l[1]]].append(
                    Node(node_color_map[l[5] + l[6]], int(l[4]))
                )
            graph[node_color_map[l[0] + l[1]]].append(
                Node(node_color_map[l[9] + l[10]], int(l[8]))
            )
            graph[node_color_map[l[0] + l[1]]].append(
                Node(node_color_map[l[13] + l[14]], int(l[12]))
            )
            graph[node_color_map[l[0] + l[1]]].append(
                Node(node_color_map[l[17] + l[18]], int(l[16]))
            )
        except IndexError:
            pass

    return graph, node_color_map


def find_parents(graph, search_node):
    parent_nodes = []

    for i in range(len(graph)):
        for item in graph[i]:
            if search_node == item.id:
                parent_nodes.append(i)
                parent_nodes.extend(find_parents(graph, i))

    return parent_nodes


def start_search(graph, search_node):
    bag_count = 0

    for child_node in graph[search_node]:
        bag_count += child_node.qty * find_children(graph, child_node.id)

    return bag_count


def find_children(graph, search_node):
    bag_count = 1

    for child_node in graph[search_node]:
        bag_count += child_node.qty * find_children(graph, child_node.id)

    return bag_count


if __name__ == "__main__":
    graph, node_color_map = make_graph(read_input())
    print(f"Part 1: {len(set(find_parents(graph, node_color_map['shinygold'])))}")  # Correct answer: 213
    print(f"Part 2: {start_search(graph, node_color_map['shinygold'])}")  # Correct answer: 38426
