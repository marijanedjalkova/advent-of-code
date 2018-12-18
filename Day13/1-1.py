from Day13.classes import Cart


def tests():
    pass


def is_cart(char):
    return char in ["V", "^", "<", ">"]


def get_road_of_direction(char):
    return "-" if char in ["<", ">"] else "|"


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
                if is_cart(char):
                    carts.append(Cart(row, col, char))
                    road_map[row][col] = get_road_of_direction(char)
                else:
                    road_map[row][col] = char
                col += 1
            row += 1
    return road_map, carts


def main():
    road_map, carts = read_in_input("input.txt")
    print(carts)


if __name__ == "__main__":
    tests()
    main()