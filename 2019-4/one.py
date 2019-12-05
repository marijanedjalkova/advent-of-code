def has_adjacent_digits(password, strict=False):
    for digit in password:
        count = password.count(digit)
        if not strict and count >= 2:
            return True
        if strict and count == 2:
            return True
    return False


def last_requirement(number):
    return has_adjacent_digits(number, True)


def is_ok(password, ignore_range_rule=False):
    if not len(password) == 6:
        return False
    if not ignore_range_rule and not int(password) in range(153517, 630395):
        return False
    if not password == ''.join(sorted(password)):
        return False
    if not has_adjacent_digits(password):
        return False
    return True


def is_ok_2(password, ignore_range_rule=False):
    return is_ok(password, ignore_range_rule) and last_requirement(password)


def get_num_of_passwords(min_value, max_value, is_pt_2=False):
    counter = 0
    for password in range(int(min_value), int(max_value) + 1):
        if not is_pt_2 and is_ok(str(password)):
            counter += 1
        elif is_pt_2 and is_ok_2(str(password)):
            counter += 1
    return counter


if __name__ == '__main__':
    puzzle_input = "153517-630395"
    min_value, max_value = puzzle_input.split("-")
    password_number = get_num_of_passwords(min_value, max_value)
    print("PT 1: ", password_number)  # 1729
    password_number = get_num_of_passwords(min_value, max_value, True)
    print("PT 2: ", password_number)  # 1172
