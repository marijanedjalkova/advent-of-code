from Day13.classes import Cart


def tests():
    collisions = find_collisions("test-input.txt")
    assert 7, 3 == collisions
    _, remaining_cart = find_collisions2("test-input2.txt")
    assert 6 == remaining_cart[0].x
    assert 4 == remaining_cart[0].y
    assert 1 == len(remaining_cart)


def is_cart(char):
    return char in ["v", "^", "<", ">"]


def get_neighbours(cart, road_map, horizontal=False):
    if not horizontal:
        return road_map[cart.x][cart.y + 1], road_map[cart.x][cart.y - 1]
    return road_map[cart.x + 1][cart.y], road_map[cart.x - 1][cart.y]


def is_on_diagonal(cart, road_map):
    neighbours = get_neighbours(cart, road_map, cart.direction in ["<", ">"])
    if neighbours[0] == neighbours[1]:
        return False
    if ("\\" in neighbours or "/" in neighbours) and neighbours[0] in ["-", "+", "|"] or neighbours[1] in ["-", "+", "|"]:
        return False
    if "+" in neighbours and "/" not in neighbours and "\\" not in neighbours:
        return False
    return True


def get_road_of_direction(cart, road_map):
    switcher = {
        "^": "\\" if cart.x + 1 in road_map and cart.y in road_map[cart.x + 1] else "/",
        "v": "/" if cart.x + 1 in road_map and cart.y in road_map[cart.x + 1] else "\\",
        "<": "\\" if cart.x in road_map and cart.y + 1 in road_map[cart.x] else "/",
        ">": "/" if cart.x in road_map and cart.y + 1 in road_map[cart.x] else "\\"
    }
    if is_on_diagonal(cart, road_map):
        result = switcher[cart.direction]
        print(Cart, cart, "is on", result)
        return result
    else:
        result = "-" if cart.direction in ["<", ">"] else "|"
        print(Cart, cart, "is on", result)
        return result


def check_collision(carts):
    locations = set()
    for cart in carts:
        if (cart.x, cart.y) in locations:
            return cart.x, cart.y
        locations.add((cart.x, cart.y))
    return None


def find_collision_carts(carts):
    locations = {}
    collisions = []
    for cart in carts:
        if (cart.x, cart.y) in locations:
            collisions.append(cart)
            collisions.append(locations[cart.x, cart.y])
            print("COLLISION AT ", cart.x, cart.y)
        locations[cart.x, cart.y] = cart
    return collisions


def tick(road_map, carts):
    for cart in carts:
        cart.make_step(road_map)


def read_in_input(filename):
    road_map = {}
    carts = []
    max_x = 0
    with open(filename) as text_input:
        contents = text_input.read().split("\n")
        row = 0
        for line in contents:
            col = 0
            for char in line:
                if col not in road_map:
                    road_map[col] = {}
                road_map[col][row] = None
                if is_cart(char):
                    carts.append(Cart(str(row+col), col, row, char))
                elif char != " ":
                    road_map[col][row] = char
                col += 1
            row += 1
            max_x = col
        max_y = row
    return road_map, carts, max_x, max_y


def place_carts(road_map, carts):
    for cart in carts:
        road_map[cart.x][cart.y] = get_road_of_direction(cart, road_map)


def print_map(road_map, carts, max_x, max_y):
    msg = None
    for row_pos in range(max_y):
        row = ""
        for col_pos in range(max_x):
            road_char = road_map[col_pos][row_pos]
            maybe_cart = list(filter(lambda cart: cart.x == col_pos and cart.y == row_pos, carts))
            if len(maybe_cart) == 1:
                row += maybe_cart[0].direction
            elif len(maybe_cart) > 1:
                row += "X"
            elif road_char is None:
                row += " "
            else:
                row += road_char
        print(row)
    if msg:
        print(msg)
        return msg[1:]
    return None


def find_collisions(filename):
    road_map, carts, max_x, max_y = read_in_input(filename)
    place_carts(road_map, carts)
    collisions = None
    while collisions is None:
        tick(road_map, carts)
        collisions = check_collision(carts)
        if collisions:
            return collisions
    return collisions


def find_collisions2(filename):
    road_map, carts, max_x, max_y = read_in_input(filename)
    place_carts(road_map, carts)
    collided = None
    while len(carts) > 1:
        tick(road_map, carts)
        collided = find_collision_carts(carts)
        if len(collided) > 0:
            for cart in collided:
                carts.remove(cart)
    return collided, carts


def main():
    collisions = find_collisions("input.txt")
    print("Answer to part 1", collisions)
    assert 8, 9 == collisions
    collisions, remaining_carts = find_collisions2("input.txt")
    print(remaining_carts)
    print(remaining_carts[0].route)
    # not 138,74
    # not 137,74
    # not 139,74


if __name__ == "__main__":
    tests()
    main()
