def get_route_points(route):
    points = set()
    current_x, current_y = 0, 0
    for instruction in route:
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == "U":
            for i in range(steps):
                current_y -= 1
                points.add((current_x, current_y))
        elif direction == "D":
            for i in range(steps):
                current_y += 1
                points.add((current_x, current_y))
        elif direction == "L":
            for i in range(steps):
                current_x -= 1
                points.add((current_x, current_y))
        elif direction == "R":
            for i in range(steps):
                current_x += 1
                points.add((current_x, current_y))
        else:
            print("WRONG")
    return points


def get_distance(cross):
    return abs(cross[0]) + abs(cross[1])


def get_min_distance(crosses):
    return min(map(get_distance, crosses))


def get_closest_cross(first_route, second_route):
    first_points = get_route_points(first_route)
    second_points = get_route_points(second_route)
    crosses = first_points & second_points
    return get_min_distance(crosses)


if __name__ == '__main__':
    with open("input.txt") as task_input:
        contents_as_lines = task_input.read().split()
        first_route = contents_as_lines[0].split(",")
        second_route = contents_as_lines[1].split(",")
        closest_cross = get_closest_cross(first_route, second_route)
        print("FINAL", closest_cross)