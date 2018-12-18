from Day11.classes import get_hundreds, Cell, get_power_level


def tests():
    assert 0 == get_hundreds(5000)
    assert 0 == get_hundreds(90)
    assert 0 == get_hundreds(-99)
    assert 1 == get_hundreds(-100)
    assert 2 == get_hundreds(234)
    assert 4 == Cell(3, 5, 8).get_power_level()
    assert -5 == Cell(122, 79, 57).get_power_level()
    assert 0 == Cell(217, 196, 39).get_power_level()
    assert 4 == Cell(101, 153, 71).get_power_level()
    assert 4 == get_total_power([Cell(3, 5, 8)])
    assert 3 == get_total_power([Cell(3, 5, 8), Cell(122, 79, 57),
                                 Cell(217, 196, 39), Cell(101, 153, 71)])


def get_total_power(cells):
    return sum([cell.power for cell in cells])


def add_cell(x, y, existing_cells, existing_square_cells):
    if not (x, y) in existing_cells:
        new_cell = Cell(x, y)
        existing_cells[(x, y)] = new_cell
    existing_square_cells.append(existing_cells[(x, y)])


def get_square_at(x, y, existing_cells, existing_squares, power_map, size=3):
    if x in existing_squares and y in existing_squares[x]:
        new_sum = power_map[x][y]
        existing_square_cells = existing_squares[x][y]
        for delta in range(size - 1):
            add_cell(x + delta, y + size - 1, existing_cells, existing_square_cells)
            new_sum += get_power_level(x + delta, y + size - 1)
            add_cell(x + size - 1, y + delta, existing_cells, existing_square_cells)
            new_sum += get_power_level(x + size - 1, y + delta)
        add_cell(x + size - 1, y + size - 1, existing_cells, existing_square_cells)
        new_sum += get_power_level(x + size - 1, y + size - 1)
        power_map[x][y] = new_sum
        return existing_square_cells, new_sum
    existing_square_cells = []
    new_sum = 0
    for x_pos in range(x, x + size):
        for y_pos in range(y, y + size):
            add_cell(x_pos, y_pos, existing_cells, existing_square_cells)
            new_sum += get_power_level(x_pos, y_pos)
    if x not in existing_squares:
        existing_squares[x] = {}
    existing_squares[x][y] = existing_square_cells
    if x not in power_map:
        power_map[x] = {}
    power_map[x][y] = new_sum
    return existing_square_cells, new_sum


def get_top_corner(max_square):
    return min(max_square, key=lambda cell: cell.x * cell.y)


def get_max_square_of_size(size, existing_cells, existing_squares, power_map):
    max_power = 0
    max_square = None
    for x in range(1, 301 - size + 1):
        for y in range(1, 301 - size + 1):
            square, power = get_square_at(x, y, existing_cells, existing_squares, power_map, size)
            if power > max_power:
                max_power = power
                max_square = (x, y)
    return max_square, max_power


def main():
    existing_cells = {}
    existing_squares = {}
    power_map = {}
    top_corner, max_power = get_max_square_of_size(3, existing_cells, existing_squares, power_map)
    print("Part 1 answer:", top_corner[0], top_corner[1])
    assert (21, 61) == (top_corner[0], top_corner[1])
    existing_squares = {}
    power_map = {}
    max_power = 0
    top_corner = None
    max_size = 0
    for i in range(1, 301):
        corner, power = get_max_square_of_size(i, existing_cells, existing_squares, power_map)
        if power > max_power:
            max_power = power
            top_corner = corner
            max_size = i
    print("Answer for part2:", top_corner[0], ",", top_corner[1], ",", max_size)
    assert max_size == 12
    assert top_corner[0] == 232
    assert top_corner[1] == 251


if __name__ == "__main__":
    tests()
    main()
