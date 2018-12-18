from collections import deque


def tests():
    assert 0 == get_row_sum([], 0)
    assert 1 == get_row_sum([False, True, False], 0)
    assert 3 == get_row_sum([False, True, True], 0)
    assert -1 == get_row_sum([False, True, False], -2)
    assert 7 == get_row_sum([False, True, True], 2)
    assert "." == row_to_str([False])
    assert "#" == row_to_str([True])
    assert ".#." == row_to_str([False, True, False])
    assert deque([False, True, False]) == parse_str(".#.")
    assert deque([True]) == parse_str("#")
    assert deque([False]) == parse_str(".")
    task_input, rules = read_in_input("test-input.txt")
    result_sum = get_final_sum(20, task_input, rules)
    assert 325 == result_sum


def get_row_sum(row, left_most_coord):
    res = 0
    for i in range(len(row)):
        if row[i] is True:
            res += (i + left_most_coord)
    return res


def process_boolean_5(five_values, rules):
    five = row_to_str(five_values)
    return rules[five] if five in rules else False


def get_next_gen(boolean_row, left_most, rules):
    boolean_row.extendleft([False] * 4)
    boolean_row.extend([False] * 4)
    result_booleans = deque()
    boolean_row.rotate(1)  # to cancel the very first rotation
    for i in range(len(boolean_row) - 4):  # for every one that might actually change
        boolean_row.rotate(-1)
        current_five = [boolean_row.popleft() for i in range(5)]
        boolean_row.extendleft(reversed(current_five))
        result_booleans.append(process_boolean_5(current_five, rules))
    left_most -= 2  # because we only actually processed 2 of each 4 pads
    empty_spaces = 0
    while result_booleans[0] is False:
        empty_spaces += 1
        result_booleans.popleft()
    left_most += empty_spaces
    while result_booleans[-1] is False:
        result_booleans.pop()
    return result_booleans, left_most


def parse_str(line):
    return deque(map(lambda char: True if char == "#" else False, line))


def row_to_str(row):
    return "".join(list(map(lambda char: "#" if char is True else ".", row)))


def get_final_sum(num_generations, row, rules):
    boolean_row = deque(parse_str(row))
    left_most_coord = 0
    for i in range(num_generations):
        boolean_row, left_most_coord = get_next_gen(boolean_row, left_most_coord, rules)
    return get_row_sum(boolean_row, left_most_coord)


def read_in_input(filename):
    with open(filename) as text_input:
        contents = text_input.read().split("\n")
        task_input = deque(contents[0].replace("initial state: ", ""))
        rest = contents[2:]
        rules = {}
        for line in rest:
            rule_input, rule_output = line.split(" => ")
            rules[rule_input] = parse_str(rule_output)[0]
        return task_input, rules


def main():
    task_input, rules = read_in_input("input.txt")
    result_sum = get_final_sum(20, task_input, rules)
    print("Answer for part1", result_sum)
    assert 2736 == result_sum


if __name__ == "__main__":
    tests()
    main()
