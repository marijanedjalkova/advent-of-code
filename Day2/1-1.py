def main():
    with open("input.txt") as input:
        codes_array = input.read().split()
        twos = threes = 0
        for code in codes_array:
            currentTwos, currentThrees = getTwosAndThrees(code)
            twos += int(currentTwos)
            threes += int(currentThrees)
        print("Checksum:", twos*threes)

def getTwosAndThrees(line):
    hashset = {}
    twosExist = threesExist = False
    for char in line:
        if char in hashset:
            hashset[char] += 1
        else:
            hashset[char] = 1
    values = hashset.values()
    return int(2 in values), int(3 in values)

if __name__ == '__main__':
    main()
