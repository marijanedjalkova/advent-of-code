OFFSET_INDEX = 2
SIZE_INDEX = 3


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split("\n")
        claimed = set()
        overlaps = set()
        for input_line in content_array:
            input_line_array = input_line.split()
            if len(input_line_array) == 0:
                continue
            claim_left_offset, claim_top_offset = list(map(int, (input_line_array[OFFSET_INDEX][:-1]).split(',')))
            claim_length, claim_height = list(map(int, (input_line_array[SIZE_INDEX]).split('x')))
            for row in range(claim_top_offset, claim_top_offset + claim_height):
                for col in range(claim_left_offset, claim_left_offset + claim_length):
                    point_id = get_point_id(row, col)
                    if point_id in claimed:
                        overlaps.add(point_id)
                    else:
                        claimed.add(point_id)
        print("Overlaps:", len(overlaps))


def get_point_id(row, col):
    return str(row) + "x" + str(col)


if __name__ == '__main__':
    main()
