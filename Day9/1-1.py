import re


def is_multiple_of(number, base):
    return not number % base


def get_counter_clockwise(circle, current_index, how_many):
    new_index = current_index - how_many
    if new_index < 0:
        new_index = len(circle) + new_index
    return new_index


def put_next(circle, current_index, next_number):
    if not is_multiple_of(next_number, 23):
        new_index = current_index + 2
        if new_index >= len(circle) + 1:
            new_index -= len(circle)
        circle.insert(new_index, next_number)
        return circle, new_index, 0
    # number is multiple of 23
    score_increase = next_number
    remove_index = get_counter_clockwise(circle, current_index, 7)
    marble_to_remove = circle[remove_index]
    score_increase += marble_to_remove
    circle.remove(marble_to_remove)
    new_index = remove_index if remove_index < len(circle) else 0
    return circle, new_index, score_increase


def tests():
    assert is_multiple_of(46, 23)
    assert not is_multiple_of(5, 2)
    assert ([0, 2, 1], 1, 0) == put_next([0, 1], 1, 2)
    assert ([0, 2, 1, 3], 3, 0) == put_next([0, 2, 1], 1, 3)
    assert ([0, 4, 2, 1, 3], 1, 0) == put_next([0, 2, 1, 3], 3, 4)
    assert 2 == get_counter_clockwise([1, 2, 3], 0, 1)
    assert 0 == get_counter_clockwise([1, 2, 3], 1, 1)
    assert ([0, 2, 3, 4, 5, 6, 7], 1, 24) == put_next([0, 1, 2, 3, 4, 5, 6, 7], 0, 23)


def main():
    with open("input.txt") as task_input:
        contents = task_input.read()
        num_players, num_rounds = get_input_data_from_input_string(contents)
        scores = {player: 0 for player in range(num_players)}
        circle = [0]
        current_index = 0
        next_number = 1
        for a_round in range(num_rounds):
            circle, new_index, score_increase = put_next(circle, current_index, next_number)
            current_index = new_index
            scores[a_round % num_players] += score_increase
            next_number += 1
        answer = max(scores.values())
        print("Answer to part 1:", answer)


def get_input_data_from_input_string(contents):
    input_data = string_to_dict(contents, "{num_players} players; last marble is worth {num_rounds} points")
    return int(input_data["num_players"]), int(input_data["num_rounds"])


def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    _dict = dict(zip(keys, values))
    return _dict


if __name__ == "__main__":
    tests()
    main()
