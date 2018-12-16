from string import ascii_lowercase


def eof(initial_length, current_position, current_length):
    return current_length == 0 or current_position >= initial_length - 1 or current_position >= current_length - 1


def are_polarised(l, r):
    return r.upper() == l.upper() and r != l


def remove_at(cursor, data):
    return data[:cursor] + data[cursor + 2:]


def get_two_chars_at(cursor, contents):
    return contents[cursor:cursor + 2]


def no_polarized(contents):
    for pair in zip(contents, contents[1:]):
        if are_polarised(pair[0], pair[1]):
            return False
    return True


def un_polarise_polymer(contents):
    initial_length = len(contents)
    cursor = 0
    current_length = initial_length
    while not eof(initial_length, cursor, current_length):
        # compare with the one in front of it
        l, r = get_two_chars_at(cursor, contents)
        while are_polarised(l, r):
            contents = remove_at(cursor, contents)
            if cursor != 0:
                cursor -= 1
            current_length -= 2
            if not (eof(initial_length, cursor, current_length)):
                l, r = get_two_chars_at(cursor, contents)
            else:
                break
        cursor += 1
    return contents


def remove_all(letter, contents):
    return ''.join([x for x in contents if x not in [letter, letter.upper()]])


def main():
    with open("input.txt") as task_input:
        contents = task_input.read()[:-1]
        shortened = un_polarise_polymer(contents)
        part_one_answer = len(shortened)
        print("Task 1 answer:", part_one_answer)
        assert(9822 == part_one_answer)
        # part 2 starting here
        results = {}
        for letter in ascii_lowercase:
            without_letter = remove_all(letter, contents)
            shortened_without_letter = un_polarise_polymer(without_letter)
            results[letter] = len(shortened_without_letter)
        part_two_answer = min(results.values())
        print("Part 2 answer:", part_two_answer)
        assert(5726 == part_two_answer)


def tests():
    assert (are_polarised("a", "A"))
    assert (are_polarised("A", "a"))
    assert (not are_polarised("a", "a"))
    assert (not are_polarised("A", "A"))
    assert (not are_polarised("a", "b"))
    assert (eof(2, 1, 5))
    assert (eof(5, 1, 2))
    assert (eof(1, 1, 5))
    assert (not eof(2, 0, 5))
    assert (not eof(3, 1, 5))
    assert ("bn" == remove_at(1, "baAn"))
    assert ("n" == remove_at(0, "aAn"))
    assert ("b" == remove_at(1, "baA"))
    assert (no_polarized("abaaB"))
    assert (not no_polarized("bbB"))
    assert (not no_polarized("abaAB"))
    assert ("" == un_polarise_polymer("abBA"))
    assert ("" == un_polarise_polymer("abcdDCBA"))
    assert ("n" == un_polarise_polymer("abcdDCBAn"))
    assert ("n" == un_polarise_polymer("nabcdDCBA"))
    assert ("" == remove_all("a", "aA"))
    assert ("nnn" == remove_all("a", "nanAn"))


if __name__ == '__main__':
    tests()
    main()
