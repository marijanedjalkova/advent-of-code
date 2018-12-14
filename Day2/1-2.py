from functools import reduce
from operator import add


def main():
    with open("input.txt") as task_input:
        codes_array = task_input.read().split()
        current_first_index = 0
        for code in codes_array:
            for code2 in codes_array[current_first_index + 1:]:
                if count_diff_characters(code, code2) == 1:
                    return get_common_part(code, code2)
            current_first_index += 1


def count_diff_characters(code1, code2):
    compare_elements = lambda x, y: 0 if (x == y) else 1
    m1 = map(compare_elements, code1, code2)
    return reduce(add, m1)


def get_common_part(code1, code2):
    common_or_none = lambda x, y: x if (x == y) else ""
    only_common = map(common_or_none, code1, code2)
    return reduce(add, only_common)


if __name__ == '__main__':
    common_code = main()
    print("Final result", common_code)
