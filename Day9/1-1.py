def is_multiple_of(number, base):
    return not number % base


def put_next(circle, current_index, next_number):
    if not is_multiple_of(next_number, 23):
        new_index = current_index + 2
        if new_index >= len(circle) + 1:
            new_index -= len(circle)
        circle.insert(new_index, next_number)
        return circle, new_index, 0
    # number is multiple of 23
    score_increase = next_number
    number_to_remove_index = get_counter_clockwise(circle, current_index, 7)
    marble_to_remove = circle[number_to_remove_index]
    score_increase += marble_to_remove
    circle.remove(marble_to_remove)
    new_index = get_next_clockwise_after_deletion(number_to_remove_index)
    return circle, new_index, score_increase


def tests():
    assert is_multiple_of(46, 23)
    assert not is_multiple_of(5, 2)
    assert ([0, 2, 1], 1, 0) == put_next([0, 1], 1, 2)
    assert ([0, 2, 1, 3], 3, 0) == put_next([0, 2, 1], 1, 3)
    assert ([0, 4, 2, 1, 3], 1, 0) == put_next([0, 2, 1, 3], 3, 4)


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split()


if __name__ == "__main__":
    tests()
    main()
