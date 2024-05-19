from sys import argv
from typing import NamedTuple


Vertex = NamedTuple("Vertex", [("x", int), ("y", int), ("z", int)])
Face = NamedTuple("Face", [("a", Vertex), ("b", Vertex), ("c", Vertex), ("d", Vertex)])


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def make_faces(x: int, y: int, z: int):
    # Make all faces of a cube given the origin of the cube
    a = Vertex(x, y, z)
    b = Vertex(x + 1, y, z)
    c = Vertex(x + 1, y + 1, z)
    d = Vertex(x, y + 1, z)
    e = Vertex(x, y, z + 1)
    f = Vertex(x + 1, y, z + 1)
    g = Vertex(x + 1, y + 1, z + 1)
    h = Vertex(x, y + 1, z + 1)

    return (
        Face(a, d, h, e),
        Face(b, c, g, f),
        Face(a, b, f, e),
        Face(d, c, g, h),
        Face(a, b, c, d),
        Face(e, f, g, h)
    )


def part_1(data):
    cube_origins = process_data(data)
    lava_droplet_surface = []
    for origin in cube_origins:
        # print(origin)
        for face in make_faces(origin.x, origin.y, origin.z):
            # print(lava_droplet_surface)
            # print(face)
            # print()
            if face in lava_droplet_surface:
                # print(f"True ({face})")
                lava_droplet_surface.remove(face)
            else:
                # print(f"False ({face})")
                lava_droplet_surface.append(face)
    # lava_droplet_surface.sort()
    # for face in lava_droplet_surface:
    #     print(face)
    print(f"Part 1: {len(lava_droplet_surface)}")


def process_data(input: list[str]) -> list[Vertex]:
    output = []
    for item in input:
        x, y, z = item.split(",")
        output.append(Vertex(int(x), int(y), int(z)))
    return output


def part_2(data):
    print(f"Part 2: {None}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 4242
    part_2(data)  # Correct answer: 