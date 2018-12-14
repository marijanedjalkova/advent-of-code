from functools import reduce
from operator import add

def main():
    with open("input.txt") as input:
        codes_array = input.read().split()
        current_first_index = 0
        for code in codes_array:
            for code2 in codes_array[current_first_index + 1:]:
                if countDiffCharacters(code, code2) == 1:
                    return getCommonPart(code, code2)
            current_first_index += 1

def countDiffCharacters(code1, code2):
    compareElements = lambda x,y: 0 if (x == y) else 1
    m1 = map(compareElements, code1, code2)
    return reduce(add, m1)

def getCommonPart(code1, code2):
    commonOrNone = lambda x,y: x if (x == y) else ""
    onlyCommon = map(commonOrNone, code1, code2)
    return reduce(add, onlyCommon)


if __name__ == '__main__':
    commonCode = main()
    print("Final result", commonCode)
