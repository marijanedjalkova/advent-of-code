import re
import sys

from Day10.classes import Point


def tests():
    point = Point(0, 1, -2, +3)
    assert (-2, 4) == point.get_pos_at_time(1)
    assert (0, 1) == point.get_pos_at_time(0)
    point2 = Point(1, 2, -2, -3)
    point3 = Point(2, 3, 0, 0)
    point4 = Point(1, 1, 0, 0)
    assert "##.\n.#.\n..#" == draw_map([point, point2, point3, point4])
    assert ".#...\n.....\n...#.\n.....\n....#\n#...." == draw_map([point, point2, point3, point4], 1)


def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    _dict = dict(zip(keys, values))
    return _dict


def get_points_map(points, time):
    point_map = {}
    for point in points:
        x, y = point.get_pos_at_time(time)
        if x in point_map:
            point_map[x].add(y)
        else:
            point_map[x] = set()
            point_map[x].add(y)
    return point_map


def map_to_drawing(pt_map):
    sz, min_max_values = get_map_size(point_map=pt_map)
    drawing = ""
    for y in range(min_max_values["min_y"], min_max_values["max_y"] + 1):
        row = ""
        for x in range(min_max_values["min_x"], min_max_values["max_x"] + 1):
            if x in pt_map and y in pt_map[x]:
                row += "#"
            else:
                row += "."
        drawing += row + "\n"
    return drawing[:-1]


def draw_map(points, time=0):
    point_map = get_points_map(points, time)
    return map_to_drawing(point_map)


def get_map_size(points=None, point_map=None, time=0):
    if point_map is None:
        point_map = get_points_map(points, time)
    min_x = min(point_map)
    max_x = max(point_map)
    min_y = min(min(point_map[x]) for x in point_map)
    max_y = max(max(point_map[x]) for x in point_map)
    return (max_x - min_x) * (max_y - min_y), {"max_x": max_x, "min_x": min_x, "max_y": max_y, "min_y": min_y}


def main():
    with open("input.txt") as task_input:
        contents = task_input.read().split("\n")
        points = []
        for line in contents:
            line = "".join(line.split())
            data_map = string_to_dict(line.strip(), "position=<{x_pos},{y_pos}>velocity=<{x_v},{y_v}>")
            points.append(
                Point(int(data_map["x_pos"]), int(data_map["y_pos"]), int(data_map["x_v"]), int(data_map["y_v"])))
        print("Read all the data")
        min_time = 0
        min_size = sys.maxsize
        for i in range(20000):
            size, _ = get_map_size(points, time=i)
            if size < min_size:
                min_size = size
                min_time = i
        print("Time it would take to appear:", min_time)
        assert (549 == min_size)
        assert (10634 == min_time)
        print(draw_map(points, min_time))


if __name__ == "__main__":
    tests()
    main()
