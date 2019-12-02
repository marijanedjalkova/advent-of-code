def run_program(list_contents):
    current_instruction = 0
    current_address = 0
    while current_address < len(list_contents):
        for pointer in range(4):
            current_address = current_instruction * 4
        op_code = list_contents[current_address]
        if op_code == 1:
            first_number = list_contents[list_contents[current_address + 1]]
            second_number = list_contents[list_contents[current_address + 2]]
            resulting_position = list_contents[current_address + 3]
            list_contents[resulting_position] = first_number + second_number
        elif op_code == 2:
            first_number = list_contents[list_contents[current_address + 1]]
            second_number = list_contents[list_contents[current_address + 2]]
            resulting_position = list_contents[current_address + 3]
            list_contents[resulting_position] = first_number * second_number
        else:
            return list_contents
        current_instruction += 1
    return list_contents


if __name__ == '__main__':
    print(list(range(4)))
    with open("input.txt") as task_input:
        contents = task_input.read().split(",")
        contents = list(map(int, contents))
        contents[1] = 12
        contents[2] = 2
        print(contents)
        output = run_program(contents)
        print(output[0])
