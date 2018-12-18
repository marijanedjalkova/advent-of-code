def get_power_level(x, y, serial_number=6042):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    result = get_hundreds(power_level) - 5
    return result


def get_hundreds(number):
    if -100 < number < 100:
        return 0
    return int(str(number)[-3])
