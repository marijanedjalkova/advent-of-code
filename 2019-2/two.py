from one import run_program


def place_noun_verb(input_list, noun, verb):
    input_list[1] = noun
    input_list[2] = verb


def get_result(input_list):
    for noun in range(99):
        for verb in range(99):
            list_copy = input_list.copy()
            place_noun_verb(list_copy, noun, verb)
            if run_program(list_copy)[0] == 19690720:
                return noun * 100 + verb
    return None


if __name__ == '__main__':
    with open("input.txt") as task_input:
        contents = task_input.read().split(",")
        contents = list(map(int, contents))
        result = get_result(contents)
        print(result)
