import re
from operator import attrgetter

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
                before_node = nodes[before_value] if before_value in nodes else None
                after_node = nodes[after_value] if after_value in nodes else None
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
        print_steps(nodes)


def is_available(child, prev):
    return all([parent.value in prev for parent in child.parents])


def print_steps(nodes):
    available = set([nodes[node] for node in nodes if len(nodes[node].parents) == 0])
    steps = []
    while(len(available)) > 0:
        print("available", available)
        next_node = choose_next_from_available(available)
        print(next_node.value)
        steps.append(next_node.value)
        for child in next_node.children:
            # only add the child if all is parents are in steps
            if is_available(child, steps):
                available.add(child)
        available.remove(next_node)
    print("".join(steps))


def choose_next_from_available(nodes):
    return min(nodes, key=attrgetter('value'))


if __name__ == "__main__":
    tests()
    main()
