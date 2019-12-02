from one import get_mass


def get_mass_with_fuel(module_mass):
    fuel_mass = get_mass(module_mass)
    total_fuel = fuel_mass
    while fuel_mass > 0:
        fuel_mass = get_mass(fuel_mass)
        if fuel_mass < 0:
            fuel_mass = 0
        total_fuel += fuel_mass
    return total_fuel


if __name__ == '__main__':
    with open("input.txt") as task_input:
        contents = task_input.read().split()
        total_mass = 0
        for module in contents:
            total_mass += get_mass_with_fuel(module)
        print(total_mass)
