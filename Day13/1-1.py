from Day13.classes import Cart


def tests():
    pass


def is_cart(char):
    return char in ["V", "^", "<", ">"]


def get_neighbours(cart, road_map, horizontal=False):
    if not horizontal:
        return road_map[cart.x][cart.y + 1], road_map[cart.x][cart.y - 1]
    return road_map[cart.x + 1][cart.y], road_map[cart.x - 1][cart.y]


def is_on_diagonal(cart, road_map):
    neighbours = get_neighbours(cart, road_map, cart in ["<", ">"])
    return neighbours[0] != neighbours[1]


def get_road_of_direction(cart, road_map):
    switcher = {
        "^": "\\" if road_map[cart.x + 1][cart.y] else "/",
        "V": "/" if road_map[cart.x + 1][cart.y] else "\\",
        "<": "\\" if road_map[cart.x][cart.y + 1] else "/",
        ">": "/" if road_map[cart.x][cart.y + 1] else "\\"
    }
    if is_on_diagonal(cart, road_map):
        return switcher[cart.direction]
    else:
        return "-" if cart.direction in ["<", ">"] else "|"


def tick(road_map, carts):
    for cart in carts:
        pass


def read_in_input(filename):
    road_map = {}
    carts = []
    with open(filename) as text_input:
        contents = text_input.read().split("\n")
        row = 0
        for line in contents:
            col = 0
            for char in line:
                if row not in road_map:
                    road_map[row] = {}
                road_map[row][col] = None
                if is_cart(char):
                    carts.append(Cart(row, col, char))
                elif char != " ":
                    road_map[row][col] = char
                col += 1
            row += 1
    return road_map, carts


def place_carts(road_map, carts):
    for cart in carts:
        road_map[cart.x][cart.y] = get_road_of_direction(cart, road_map)


def main():
    road_map, carts = read_in_input("input.txt")
    place_carts(road_map, carts)
    print(carts)


if __name__ == "__main__":
    tests()
    main()
