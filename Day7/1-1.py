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


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split("\n")
        nodes = {}
        for line in content_array:
            before_value, after_value = extract_before_and_after_from_string(line)
            before_node = nodes[before_value] if before_value in nodes else create_node_put_in_map(before_value, nodes)
            after_node = nodes[after_value] if after_value in nodes else create_node_put_in_map(after_value, nodes)
            common_parents = set(before_node.parents).intersection(after_node.parents)
            for common_parent in common_parents:
                after_node.parents.remove(common_parent)
                common_parent.children.remove(after_node)
            before_node.add_child(after_node)
            after_node.add_parent(before_node)
        print_steps(nodes)


def create_node_put_in_map(value, nodes):
    node = Node(value)
    nodes[value] = node
    return node


def is_available(child, prev):
    return all([parent.value in prev for parent in child.parents])


def print_steps(nodes):
    available = set([nodes[node] for node in nodes if len(nodes[node].parents) == 0])
    steps = []
    while(len(available)) > 0:
        next_node = choose_next_from_available(available)
        steps.append(next_node.value)
        for child in next_node.children:
            # only add the child if all is parents have executed
            if is_available(child, steps):
                available.add(child)
        available.remove(next_node)
    answer = "".join(steps)
    assert ("ACHOQRXSEKUGMYIWDZLNBFTJVP" == answer)


def choose_next_from_available(nodes):
    return min(nodes, key=attrgetter('value'))


if __name__ == "__main__":
    tests()
    main()
