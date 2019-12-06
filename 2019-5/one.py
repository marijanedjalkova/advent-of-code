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


def run_programs(list_contents, input_value=None, pt2=False):
    instruction_pointer = 0
    output = 0
    while instruction_pointer < len(list_contents):
        instruction_starter = list_contents[instruction_pointer]
        print(list_contents)
        print("Instruction pointer ", instruction_pointer, len(list_contents))
        print("starter -", instruction_starter, "-")
        if int(str(instruction_starter)) == 99:
            print("OUTPUT")
            return output
        op_code = int(str(instruction_starter)[-2:])
        if op_code == 1:
            parameters = get_parameters(3, instruction_starter, list_contents, instruction_pointer)
            resulting_position = int(list_contents[instruction_pointer + 3])
            list_contents[resulting_position] = str(int(parameters[0]) + int(parameters[1]))
            instruction_pointer += 4
            continue
        elif op_code == 2:
            parameters = get_parameters(3, instruction_starter, list_contents, instruction_pointer)
            resulting_position = int(list_contents[instruction_pointer + 3])
            list_contents[resulting_position] = int(parameters[0]) * int(parameters[1])
            instruction_pointer += 4
            continue
        elif op_code == 3:
            print("PLEASE PROVIDE INPUT")
            if input_value is None:
                input_str = input()
            else:
                input_str = str(input_value)
            print("INPUT IS ", input_str)
            list_contents[int(list_contents[instruction_pointer + 1])] = input_str
            instruction_pointer += 2
        elif op_code == 4:
            parameters = get_parameters(1, instruction_starter, list_contents, instruction_pointer)
            output = parameters[0]
            print("OUTPUT", output)
            instruction_pointer += 2
        elif op_code == 5 and pt2:
            # 2 parameters
            parameters = get_parameters(2, instruction_starter, list_contents, instruction_pointer)
            if int(parameters[0]) != 0:
                instruction_pointer = int(parameters[1])
                print("New pointer 5 is ", instruction_pointer)
            else:
                instruction_pointer += 3
        elif op_code == 6 and pt2:
            # 2 parameters
            parameters = get_parameters(2, instruction_starter, list_contents, instruction_pointer)
            if int(parameters[0]) == 0:
                instruction_pointer = int(parameters[1])
                print("New pointer 6 is ", instruction_pointer)
            else:
                instruction_pointer += 3
        elif op_code == 7 and pt2:
            # 3 parameters
            parameters = get_parameters(3, instruction_starter, list_contents, instruction_pointer)
            if int(parameters[0]) < int(parameters[1]):
                list_contents[int(parameters[2])] = "1"
            else:
                list_contents[int(parameters[2])] = "0"
            instruction_pointer += 4
        elif op_code == 8 and pt2:
            # 3 parameters
            parameters = get_parameters(3, instruction_starter, list_contents, instruction_pointer)
            if int(parameters[0]) == int(parameters[1]):
                list_contents[int(parameters[2])] = "1"
            else:
                list_contents[int(parameters[2])] = "0"
            instruction_pointer += 4
        else:
            print("UNRECOGNIZED OP CODE ", op_code)
            return
    print("Not sure eof is reached")
    return output


if __name__ == '__main__':
    with open("input.txt") as puzzle_input:
        numbers = puzzle_input.read().split(",")
        program_result = run_programs(numbers, 1)  # Pt 1output is 7157989
        print("PT 1: ", program_result)
        program_result2 = run_programs(numbers, 5, True)
        print("PT 2: ", program_result2)
