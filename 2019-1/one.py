import math


def get_mass(module_mass):
    return math.floor(int(module_mass) / 3) - 2


if __name__ == '__main__':
    with open("input.txt") as task_input:
        contents = task_input.read().split()
        total_mass = 0
        for module in contents:
            total_mass += get_mass(module)
        print(total_mass)
