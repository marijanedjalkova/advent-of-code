def get_parameter(mode, list_contents, instruction_pointer, parameter_index):
    if mode == "0":  # position mode
        return list_contents[int(list_contents[instruction_pointer + parameter_index])]
    return list_contents[instruction_pointer + parameter_index]


def get_parameters(size, instruction_starter, list_contents, instruction_pointer):
    modes = list(reversed(instruction_starter[:-2]))
    while (len(modes)) < size:
        modes += "0"
    parameters = []
    for parameter_index in range(1, size + 1):
        mode = modes[parameter_index - 1]
        parameter = get_parameter(mode, list_contents, instruction_pointer, parameter_index)
        parameters.append(parameter)
    return parameters


def run_program(list_contents):
    instruction_pointer = 0
    while instruction_pointer < len(list_contents):
        instruction_starter = list_contents[instruction_pointer]
        print(list_contents)
        print("Instruction pointer ", instruction_pointer, len(list_contents))
        print("starter ", instruction_starter)
        op_code = str(instruction_starter)[-2:]
        if int(op_code) == 1:
            parameters = get_parameters(3, instruction_starter, list_contents, instruction_pointer)
            resulting_position = int(list_contents[instruction_pointer + 3])
            list_contents[resulting_position] = str(int(parameters[0]) + int(parameters[1]))
            instruction_pointer += 4
            continue
        elif int(op_code) == 2:
            parameters = get_parameters(3, instruction_starter, list_contents, instruction_pointer)
            resulting_position = int(list_contents[instruction_pointer + 3])
            list_contents[resulting_position] = int(parameters[0]) * int(parameters[1])
            instruction_pointer += 4
            continue
        elif int(op_code) == 3:
            input_number = 1
            list_contents[int(list_contents[instruction_pointer + 1])] = str(input_number)
            instruction_pointer += 2
        elif int(op_code) == 4:
            print("OUTPUT", list_contents[int(list_contents[instruction_pointer + 1])])
            instruction_pointer += 2
        elif int(op_code) == 99:
            print("99!!!!!!")
            break
        else:
            print("UNRECOGNIZED OP CODE ", op_code)
            return list_contents
    return list_contents


if __name__ == '__main__':
    with open("input.txt") as puzzle_input:
        numbers = puzzle_input.read().split(",")
        program_result = run_program(numbers) # output is 7157989
