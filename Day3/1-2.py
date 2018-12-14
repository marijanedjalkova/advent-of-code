OFFSET_INDEX = 2
SIZE_INDEX = 3
ID_INDEX = 0


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split("\n")
        claimed_points = {}
        candidates = set()
        for input_line in content_array:
            input_line_array = input_line.split()
            if len(input_line_array) == 0:
                continue
            process_claim(claimed_points, candidates, input_line_array)
        print("Not overlapped", candidates, len(candidates))


def process_claim(claimed_points, candidates, input_line_array):
    claim_left_offset, claim_top_offset = list(map(int, (input_line_array[OFFSET_INDEX][:-1]).split(',')))
    claim_length, claim_height = list(map(int, (input_line_array[SIZE_INDEX]).split('x')))
    claim_id = input_line_array[ID_INDEX]
    claim_overlapped = (any([process_point(row, col, claimed_points, claim_id, candidates)
                             for row in range(claim_top_offset, claim_top_offset + claim_height)
                             for col in range(claim_left_offset, claim_left_offset + claim_length)]))
    if not claim_overlapped:
        candidates.add(claim_id)


def process_point(row, col, claimed_points, claim_id, candidates):
    is_overlap = False
    point_id = get_point_id(row, col)
    if point_id in claimed_points:
        is_overlap = True
        claimed_points[point_id].append(claim_id)
        update_overlaps(candidates, claimed_points[point_id])
    else:
        # no overlaps, this is the first time this spot has been claimed
        claimed_points[point_id] = [claim_id]
    return is_overlap


def update_overlaps(candidates, overlapping_claim_ids):
    for overlapping_claim_id in overlapping_claim_ids:
        if overlapping_claim_id in candidates:
            candidates.remove(overlapping_claim_id)


def get_point_id(row, col):
    return str(row) + "x" + str(col)


if __name__ == '__main__':
    main()
