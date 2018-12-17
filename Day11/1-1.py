from Day11.classes import get_hundreds, Cell


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
    return sum([cell.get_power_level() for cell in cells])


def get_square_at(x, y, existing_cells, size=3):
    cells = []
    for x_pos in range(x, x + size):
        for y_pos in range(y, y + size):
            if (x_pos, y_pos) in existing_cells:
                cells.append(existing_cells[(x_pos, y_pos)])
            else:
                new_cell = Cell(x_pos, y_pos)
                cells.append(new_cell)
                existing_cells[(x_pos, y_pos)] = new_cell
    return cells


def get_top_corner(max_square):
    return min(max_square, key=lambda cell: cell.x * cell.y)


def main():
    existing_cells = {}
    max_power = 0
    max_square = None
    for x in range(1, 301):
        for y in range(1, 301):
            square = get_square_at(x, y, existing_cells)
            power = get_total_power(square)
            if power > max_power:
                max_power = power
                max_square = square
    top_corner = get_top_corner(max_square)
    print("Part 1 answer:", top_corner.x, top_corner.y)
    assert (21, 61) == (top_corner.x, top_corner.y)


if __name__ == "__main__":
    tests()
    main()
