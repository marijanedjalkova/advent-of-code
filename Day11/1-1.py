from Day11.classes import get_hundreds, get_power_level
import math


def tests():
    assert 0 == get_hundreds(5000)
    assert 0 == get_hundreds(90)
    assert 0 == get_hundreds(-99)
    assert 1 == get_hundreds(-100)
    assert 2 == get_hundreds(234)
    assert 4 == get_power_level(3, 5, 8)
    assert -5 == get_power_level(122, 79, 57)
    assert 0 == get_power_level(217, 196, 39)
    assert 4 == get_power_level(101, 153, 71)


def get_square_at(x, y, power_map, size=3):
    if x in power_map and y in power_map[x]:
        if size % 2 == 0:
            # combine the sums of 4 smaller squares
            new_sum = power_map[x][y][size / 2] + power_map[x + size / 2][y][size / 2] + power_map[x][y + size / 2][size / 2] + power_map[x + size / 2][y + size / 2][size / 2]
            power_map[x][y][size] = new_sum
            return new_sum
        else:
            # say, 11. Then can take 6x6, 5x5, 5x5 and 6x6 and remove the central square
            half_and_a_bit = math.ceil(size / 2)
            almost_half = size - half_and_a_bit
            sum_top_left = power_map[x][y][half_and_a_bit]
            sum_top_right = power_map[x + half_and_a_bit][y][almost_half]
            sum_bottom_left = power_map[x][y + half_and_a_bit][almost_half]
            sum_bottom_right = power_map[x + almost_half][y + almost_half][half_and_a_bit]
            central_square = power_map[x + almost_half][y + almost_half][1]
            new_sum = sum_top_left + sum_top_right + sum_bottom_left + sum_bottom_right - central_square
            power_map[x][y][size] = new_sum
            return new_sum
    new_sum = 0
    for x_pos in range(x, x + size):
        for y_pos in range(y, y + size):
            new_sum += get_power_level(x_pos, y_pos)
    if x not in power_map:
        power_map[x] = {}
    if y not in power_map[x]:
        power_map[x][y] = {}
    power_map[x][y][size] = new_sum
    return new_sum


def get_max_square_of_size(size, power_map, board_size):
    max_power = 0
    max_square = None
    for x in range(1, board_size + 1 - size + 1):
        for y in range(1, board_size + 1 - size + 1):
            power = get_square_at(x, y, power_map, size)
            if power > max_power:
                max_power = power
                max_square = (x, y)
    return max_square, max_power


def main():
    power_map = {}
    top_corner, max_power = get_max_square_of_size(3, power_map, 300)
    print("Part 1 answer:", top_corner[0], top_corner[1])
    assert (21, 61) == (top_corner[0], top_corner[1])
    power_map = {}
    max_power = 0
    top_corner = None
    max_size = 0
    for i in range(1, 301):
        corner, power = get_max_square_of_size(i, power_map, 300)
        if power > max_power:
            max_power = power
            top_corner = corner
            max_size = i
    print("Answer for part2:", top_corner[0], ",", top_corner[1], ",", max_size)
    assert max_size == 12
    assert (232, 251) == top_corner


if __name__ == "__main__":
    tests()
    main()
