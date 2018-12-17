import re

from Day10.classes import Point


def tests():
    pass


def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    _dict = dict(zip(keys, values))
    return _dict


def draw_map(points, time=0):
    min_x = min(points, key=lambda p: p.get_pos_at_time(time).x).x
    max_x = max(points, key=lambda p: p.get_pos_at_time(time).x).x
    min_y = min(points, key=lambda p: p.get_pos_at_time(time).x).y
    max_y = max(points, key=lambda p: p.get_pos_at_time(time).x).y
    # -10406 53399 -10506 53298
    drawn = {}
    for point in points:
        if point.x in drawn:
            drawn[point.x].add(point.y)
        else:
            drawn[point.x] = set(point.y)
    for y in range(min_y, max_y):
        row = ""
        for x in range(min_x, max_x):
            if x in drawn and y in drawn[x]:
                row += "#"
            else:
                row += "."
        print(row)


def main():
    with open("input.txt") as task_input:
        contents = task_input.read().split("\n")
        points = []
        for line in contents:
            line = "".join(line.split())
            data_map = string_to_dict(line.strip(), "position=<{x_pos},{y_pos}>velocity=<{x_v},{y_v}>")
            points.append(Point(int(data_map["x_pos"]), int(data_map["y_pos"]), int(data_map["x_v"]), int(data_map["y_v"])))
        print("Read all the data")
        draw_map(points)


if __name__ == "__main__":
    tests()
    main()
