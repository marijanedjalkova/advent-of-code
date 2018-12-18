class Cell:

    def __init__(self, x, y, serial_number=6042):
        self.x = x  # 1 to 300, top left (1,1), top right (300,1)
        self.y = y
        self.serial_number = serial_number
        self.power = self.get_power_level()

    def get_power_level(self):
        rack_id = self.x + 10
        power_level = rack_id * self.y
        power_level += self.serial_number
        power_level *= rack_id
        result = get_hundreds(power_level) - 5
        return result

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


def get_power_level(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += 6042
    power_level *= rack_id
    result = get_hundreds(power_level) - 5
    return result


def get_hundreds(number):
    if -100 < number < 100:
        return 0
    return int(str(number)[-3])
