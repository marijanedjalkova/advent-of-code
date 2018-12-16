def manhattan(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def get_sum_distance_from_point(point, xs, ys):
    zipped = list(zip(xs, ys))
    return sum([manhattan(point, dot_tuple) for dot_tuple in zipped])


def get_near_area(max_distance, xs, ys):
    all_points_with_distance_sums = [get_sum_distance_from_point((x, y), xs, ys) for x in range(min(xs), max(xs)) for y
                                     in range(min(ys), max(ys))]
    return len(list(filter(lambda dist: dist < max_distance, all_points_with_distance_sums)))


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
        close_area = get_near_area(10000, xs, ys)
        print("Part2 solution", close_area)
        assert (38670 == close_area)


if __name__ == '__main__':
    main()
