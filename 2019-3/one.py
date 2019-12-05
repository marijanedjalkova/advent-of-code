def get_route_points(route):
    points = {}
    current_x, current_y = 0, 0
    counter = 1
    for instruction in route:
        direction = instruction[0]
        steps = int(instruction[1:])
        for i in range(steps):
            if direction == "U":
                current_y -= 1
            elif direction == "D":
                current_y += 1
            elif direction == "L":
                current_x -= 1
            elif direction == "R":
                current_x += 1
            else:
                print("WRONG")
            if (current_x, current_y) not in points:
                points[(current_x, current_y)] = counter
            counter += 1
    return points


def get_distance(cross):
    return abs(cross[0]) + abs(cross[1])


def get_min_distance(crosses):
    return min(map(get_distance, crosses))


def get_closest_cross(first_route, second_route):
    first_points = get_route_points(first_route)
    second_points = get_route_points(second_route)
    crosses = set(first_points.keys()) & set(second_points.keys())
    return get_min_distance(crosses)


def get_steps(points, cross):
    return points[cross]


def get_min_steps(first_route, second_route):
    first_points = get_route_points(first_route)
    second_points = get_route_points(second_route)
    crosses = set(first_points) & set(second_points)
    steps = set()
    for cross in crosses:
        steps.add(first_points[cross] + second_points[cross])
    return min(steps)


if __name__ == '__main__':
    with open("input.txt") as task_input:
        contents_as_lines = task_input.read().split()
        first_route = contents_as_lines[0].split(",")
        second_route = contents_as_lines[1].split(",")
        closest_cross = get_closest_cross(first_route, second_route)
        print("PT 1: ", closest_cross)
        min_steps = get_min_steps(first_route, second_route)
        print("PT 2: ", min_steps)
