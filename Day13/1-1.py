from Day13.classes import Cart


def tests():
    collisions = find_collisions("test-input.txt")
    assert 7, 3 == collisions


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
        "^": "\\" if road_map[cart.x + 1][cart.y] else "/",
        "v": "/" if road_map[cart.x + 1][cart.y] else "\\",
        "<": "\\" if road_map[cart.x][cart.y + 1] else "/",
        ">": "/" if road_map[cart.x][cart.y + 1] else "\\"
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


def tick(road_map, carts):
    for cart in carts:
        cart.make_step(road_map)


def read_in_input(filename):
    road_map = {}
    carts = []
    max_x = 0
    max_y = 0
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
                    carts.append(Cart(col, row, char))
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
    for row_pos in range(max_y):
        row = ""
        for col_pos in range(max_x):
            road_char = road_map[col_pos][row_pos]
            maybe_cart = list(filter(lambda cart: cart.x == col_pos and cart.y == row_pos, carts))
            if len(maybe_cart) > 0:
                row += maybe_cart[0].direction
            elif road_char is None:
                row += " "
            else:
                row += road_char
        print(row)


def find_collisions(filename):
    road_map, carts, max_x, max_y = read_in_input(filename)
    place_carts(road_map, carts)
    print_map(road_map, carts, max_x, max_y)
    collisions = None
    # counter = 0
    # while collisions is None:
    #     print(counter)
    #     tick(road_map, carts)
    #     print_map(road_map, carts)
    #     collisions = check_collision(carts)
    #     counter += 1
    return collisions


def main():
    collisions = find_collisions("input.txt")
    # not 107,95


if __name__ == "__main__":
    tests()
    # main()
