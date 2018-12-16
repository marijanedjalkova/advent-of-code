from Day8.classes import Node


def read_tree(numbers, current_index):
    num_of_children, num_of_metadata = map(int, numbers[current_index:current_index + 2])
    current_index += 2
    root = Node()
    for child_index in range(num_of_children):
        child, new_index = read_tree(numbers, current_index)
        root.add_child(child)
        current_index = new_index
    root.metadata = list(map(int, numbers[current_index: current_index + num_of_metadata]))
    return root, current_index + num_of_metadata


def calculate_tree_metadata_sum(root):
    return root.get_metadata_sum() + sum([calculate_tree_metadata_sum(child) for child in root.children])


def tests():
    parent_2_kids = [2, 2, 1, 2, 0, 3, 11, 22, 33, 66, 77, 0, 2, 88, 99, 16, 67]
    root, index = read_tree(parent_2_kids, 0)
    assert (2 == len(root.children))
    assert ([66, 77] == root.children[0].metadata)
    assert (1 == len(root.children[0].children))
    assert ([11, 22, 33] == root.children[0].children[0].metadata)
    assert ([88, 99] == root.children[1].metadata)
    assert ([16, 67] == root.metadata)
    assert (66 + 77 + 11 + 22 + 33 + 88 + 99 + 16 + 67 == calculate_tree_metadata_sum(root))


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split()
        root, new_index = read_tree(content_array, 0)
        metadata_sum = calculate_tree_metadata_sum(root)
        print("Part 1 answer:", metadata_sum)


if __name__ == "__main__":
    tests()
    main()
