OFFSET_INDEX = 2
SIZE_INDEX = 3

def main():
    with open("input.txt") as input:
        content_array = input.read().split("\n")
        claimed = set()
        overlaps = set()
        for input_line in content_array:
            input_line_array = input_line.split()
            if len(input_line_array) == 0:
                continue
            offsets = (input_line_array[OFFSET_INDEX][:-1]).split(",")
            sizes = (input_line_array[SIZE_INDEX]).split("x")
            claim_left_offset = int(offsets[0])
            claim_top_offset = int(offsets[1])
            claim_length = int(sizes[0])
            claim_height = int(sizes[1])
            for row in range(claim_top_offset, claim_top_offset + claim_height):
                for col in range(claim_left_offset, claim_left_offset + claim_length):
                    pointId = getPointId(row, col)
                    if pointId in claimed:
                        overlaps.add(pointId)
                    else: claimed.add(pointId)
        print("Overlaps:", len(overlaps))

def getPointId(row, col):
    return str(row) + "x" + str(col)

if __name__ == '__main__':
     main()
