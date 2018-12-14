def main():
    with open("input.txt") as task_input:
        codes_array = task_input.read().split()
        twos = threes = 0
        for code in codes_array:
            current_twos, current_threes = get_twos_and_threes(code)
            twos += int(current_twos)
            threes += int(current_threes)
        print("Checksum:", twos*threes)


def get_twos_and_threes(line):
    word_map = {}
    for char in line:
        if char in word_map:
            word_map[char] += 1
        else:
            word_map[char] = 1
    values = word_map.values()
    return int(2 in values), int(3 in values)


if __name__ == '__main__':
    main()
