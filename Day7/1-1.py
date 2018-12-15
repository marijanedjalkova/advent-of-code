import re

from Day7.classes import Node


def string_to_dict(string, pattern):
    regex = re.sub(r'{(.+?)}', r'(?P<_\1>.+)', pattern)
    values = list(re.search(regex, string).groups())
    keys = re.findall(r'{(.+?)}', pattern)
    _dict = dict(zip(keys, values))
    return _dict


def tests():
    assert ({"before": "X", "after": "M"} ==
            string_to_dict("Step X must be finished before step M can begin.",
                           "Step {before} must be finished before step {after} can begin."))
    # assert(find_in_flows(2, Node("3", None)) is None)
    # assert(find_in_flows(3, None) is None)
    # assert(Node("X", child=Node("M"))) == find_in_flows("X", Node("X", child=Node("M")))
    # assert (Node("M") == find_in_flows("M", Node("X", child=Node("M"))))
    # assert (Node("Y") == find_in_flows("Y", Node("X", child=Node("M", child=Node("Y")))))
    # flow = Node("X", child=Node("M", child=Node("Y")))
    # flow.add_child(Node("A"))
    # assert (Node("A") == find_in_flows("A", flow))


def extract_before_and_after_from_string(line):
    word_map = string_to_dict(line, "Step {before} must be finished before step {after} can begin.")
    return word_map["before"], word_map["after"]


def have_not_seen_before(before, after, prev):
    return before not in prev and after not in prev


# def find_in_flows(sought_value, node):
#     if node is None:
#         return None
#     if node.value == sought_value:
#         return node
#     for child in node.children:
#         found = find_in_flows(sought_value, child)
#         if found:
#             return found
#
#
# def find_among_seen(value, flows):
#     for flow in flows:
#         found = find_in_flows(value, flows[flow])
#         if found:
#             return found


def get_by_value(value, nodes):
    return nodes[value] if value in nodes else None


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split("\n")
        nodes = {}
        for line in content_array:
            print(line)
            before_value, after_value = extract_before_and_after_from_string(line)
            if have_not_seen_before(before_value, after_value, nodes):
                after = Node(after_value)
                before = Node(before_value)
                before.add_child(after)
                after.add_parent(before)
                nodes[before_value] = before
                nodes[after_value] = after
            else:
                before_node = get_by_value(before_value, nodes)
                after_node = get_by_value(after_value, nodes)
                if before_node and after_node:
                    common_parents = set(before_node.parents).intersection(after_node.parents)
                    for common_parent in common_parents:
                        after_node.parents.remove(common_parent)
                        common_parent.children.remove(after_node)
                    after_node.add_parent(before_node)
                    before_node.add_child(after_node)
                elif after_node:
                    # have not seen before but seen after
                    before_node = Node(before_value)
                    nodes[before_value] = before_node
                    after_node.add_parent(before_node)
                    before_node.add_child(after_node)
                else:
                    # seen only before_node
                    after_node = Node(after_value)
                    nodes[after_value] = after_node
                    after_node.add_parent(before_node)
                    before_node.add_child(after_node)
        print("DONE READING")
        beginning_nodes = [node for node in nodes if len(nodes[node].parents) == 0]
        beginning_nodes.sort()
        print(beginning_nodes)
        print(beginning_nodes[0])
        print(nodes[beginning_nodes[0]])


if __name__ == "__main__":
    tests()
    main()
