def run_program(list_contents):
    current_instruction = 0
    instruction_pointer = 0
    while instruction_pointer < len(list_contents):
        for pointer in range(4):
            instruction_pointer = current_instruction * 4
        op_code = list_contents[instruction_pointer]
        if op_code == 1:
            first_number = list_contents[list_contents[instruction_pointer + 1]]
            second_number = list_contents[list_contents[instruction_pointer + 2]]
            resulting_position = list_contents[instruction_pointer + 3]
            list_contents[resulting_position] = first_number + second_number
        elif op_code == 2:
            first_number = list_contents[list_contents[instruction_pointer + 1]]
            second_number = list_contents[list_contents[instruction_pointer + 2]]
            resulting_position = list_contents[instruction_pointer + 3]
            list_contents[resulting_position] = first_number * second_number
        else:
            return list_contents
        current_instruction += 1
    return list_contents


if __name__ == '__main__':
    with open("input.txt") as task_input:
        contents = task_input.read().split(",")
        contents = list(map(int, contents))
        contents[1] = 12
        contents[2] = 2
        print(contents)
        output = run_program(contents)
        print(output[0])
