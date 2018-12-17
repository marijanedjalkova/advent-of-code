import re


def is_multiple_of(number, base):
    return not number % base


def get_counter_clockwise(circle, current_index, how_many):
    new_index = current_index - how_many
    if new_index < 0:
        new_index = len(circle) + new_index
    return new_index


def get_new_index(current_index, current_length, diff):
    new_index = current_index + diff
    if new_index >= current_length + 1:
        new_index -= current_length
    return new_index


def put_next(circle, current_index, next_number):
    if not is_multiple_of(next_number, 23):
        new_index = get_new_index(current_index, len(circle), 2)
        if next_number % 23 == 19:
            return get_new_index(current_index, len(circle), 1), 0
        circle.insert(new_index, next_number)
        if next_number % 23 == 18:
            old_value = circle[new_index + 1]
            circle[new_index + 1] = next_number + 1
            return new_index, old_value
        return new_index, 0
    new_index = get_counter_clockwise(circle, current_index, 6)
    return new_index, next_number


def tests():
    assert is_multiple_of(46, 23)
    assert not is_multiple_of(5, 2)
    assert (1, 0) == put_next([0, 1], 1, 2)
    assert (3, 0) == put_next([0, 2, 1], 1, 3)
    assert (1, 0) == put_next([0, 2, 1, 3], 3, 4)
    assert 2 == get_counter_clockwise([1, 2, 3], 0, 1)
    assert 0 == get_counter_clockwise([1, 2, 3], 1, 1)


def do_game(num_players, num_rounds):
    scores = {player: 0 for player in range(num_players)}
    circle = [0]
    current_index = 0
    next_number = 1
    for a_round in range(num_rounds):
        new_index, score_increase = put_next(circle, current_index, next_number)
        if next_number % 23 == 18:
            assign_to_23rd(scores, score_increase, a_round, num_players)
            current_index = new_index
            next_number += 1
            continue
        current_index = new_index
        scores[a_round % num_players] += score_increase
        next_number += 1
    return scores


def assign_to_23rd(scores, score_increase, a_round, num_players):
    index = a_round % num_players + 5
    if index >= num_players:
        index -= num_players
    scores[index] += score_increase


def main():
    with open("input.txt") as task_input:
        contents = task_input.read()
        num_players, num_rounds = get_input_data_from_input_string(contents)
        scores = do_game(num_players, num_rounds)
        answer = max(scores.values())
        print("Answer to part 1:", answer)
        assert (398048 == answer)
        scores = do_game(num_players, num_rounds * 100)
        answer = max(scores.values())
        print("Answer to part 2:", answer)
        assert (3180373421 == answer)


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
