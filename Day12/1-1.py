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
    res = 0  # False, True, False , -2 but we want 0, 1, 2
    for i in range(len(row)):
        if row[i] is True:
            res += (i + left_most_coord)
    return res


def take_five(row, i):
    return [row[c] for c in range(i - 2, i + 3)]


def process_boolean_5(boolean_row, i, rules):
    five_values = take_five(boolean_row, i)
    five = row_to_str(five_values)
    return rules[five] if five in rules else False


def get_next_gen(boolean_row, left_most, rules):
    """
    add 4 dots on either side of the input;
    (only 2 will be affected at most but for the leftmost of the two to be affected, need two more);
    move the left-most-coord by -4;
    map input to output for range(row[2:-1]);
    record how many empty spaces at the beginning => e;
    trim the spaces at the beginning and the end;
    move the left-most-coord by +e;
    return the output together with the left-most-coord
    """
    boolean_row.extendleft([False] * 4)
    boolean_row.extend([False] * 4)
    result_booleans = deque([process_boolean_5(boolean_row, i, rules) for i in range(2, len(boolean_row) - 2)])
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
    boolean_row = parse_str(row)
    left_most_coord = 0
    print(0, 0, "".join(row))
    for i in range(num_generations):
        boolean_row, left_most_coord = get_next_gen(boolean_row, left_most_coord, rules)
        print(i+1, left_most_coord, row_to_str(boolean_row))
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
    print(rules)


if __name__ == "__main__":
    tests()
    main()
