def manhattan(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def is_at_border(point, min_x, max_x, min_y, max_y):
    x = point[0]
    y = point[1]
    return x == min_x or x == max_x or y == min_y or y == max_y


def count_closest(dot_map, dot, min_x, max_x, min_y, max_y):
    closest_to_dot = [k for k, v in dot_map.items() if v == dot]
    for point in closest_to_dot:
        if is_at_border(point, min_x, max_x, min_y, max_y):
            return "Infinity"
    return len(closest_to_dot)


def get_point_data(dot_map, xs, ys):
    res = {}
    for dot in zip(xs, ys):
        # find out how many dots in map had value == dot
        closest_amount = count_closest(dot_map, dot, min(xs), max(xs), min(ys), max(ys))
        if closest_amount != "Infinity":
            res[dot] = closest_amount
    return res


def get_closest_dot(point, dots):
    distances = {}
    for dot in dots:
        distance = manhattan(point, dot)
        if distance in distances:
            distances[distance].append(dot)
        else:
            distances[distance] = [dot]
    if len(distances[min(distances)]) > 1:
        return "."
    return distances[min(distances)][0]


def make_map(xs, ys):
    zipped = list(zip(xs, ys))
    return {(x, y): get_closest_dot((x, y), zipped) for x in range(min(xs), max(xs)) for y in range(min(ys), max(ys))}


def main():
    with open("input.txt") as task_input:
        contents = task_input.read().split("\n")
        xs = []
        ys = []
        for line in contents:
            if len(line) == 0:
                continue
            x, y = line.split(", ")
            xs.append(int(x))
            ys.append(int(y))
        data_map = make_map(xs, ys)
        results = get_point_data(data_map, xs, ys)  # point_coord: how many close_to
        max_distance = max(list(results.values()))
        print("Part 1 solution", max_distance)
        assert (5975 == max_distance)


def tests():
    assert (2 == manhattan((0, 0), (1, 1)))
    assert (1 == manhattan((0, 0), (0, 1)))
    assert (12 == manhattan((-6, -6), (0, 0)))
    assert (9 == manhattan((-3, 2), (2, -2)))
    assert ("." == get_closest_dot((0, 0), [(1, 2), (2, 1)]))
    assert ((1, 2) == get_closest_dot((0, 0), [(1, 2), (2, 2)]))


if __name__ == '__main__':
    tests()
    main()
