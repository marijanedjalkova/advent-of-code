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
    assert (1 == get_index_from_letter("A"))
    assert (26 == get_index_from_letter("Z"))
    assert (61 == get_step_length("A"))
    assert (86 == get_step_length("Z"))
    assert ([Node("0"), Node("1"), Node("3")] == choose_x_available([Node("1"), Node("3"), Node("0")], 5, {}))
    assert ([Node("0"), Node("3")] == choose_x_available([Node("1"), Node("3"), Node("0")], 5, {1: Node("1")}))


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
        get_parallel_steps(nodes)


def create_node_put_in_map(value, nodes):
    node = Node(value)
    nodes[value] = node
    return node


def is_available(child, prev):
    return all([parent.value in prev for parent in child.parents])


def print_steps(nodes):
    available = [nodes[node] for node in nodes if len(nodes[node].parents) == 0]
    steps = []
    while (len(available)) > 0:
        next_node = choose_next_from_available(available)
        steps.append(next_node.value)
        available.extend(list(filter(lambda child: is_available(child, steps), next_node.children)))
        available.remove(next_node)
    answer = "".join(steps)
    print("Answer to part 1:", answer)
    assert ("ACHOQRXSEKUGMYIWDZLNBFTJVP" == answer)


def choose_x_available(available, how_many, current_tasks):
    sorted_available = list(filter(lambda task: task not in current_tasks.values(), sorted(available, key=lambda node: node.value)))
    return sorted_available[:how_many]


def check_any_finished_tasks(current_tasks, workers_times, time, steps, available):
    if not time > 0:
        return
    for worker_data in current_tasks:
        if not current_tasks[worker_data]:
            continue
        if workers_times[worker_data] <= time:
            finished_task = current_tasks[worker_data]
            steps.append(finished_task.value)
            new_available = list(filter(lambda child: is_available(child, steps), finished_task.children))
            available.extend(new_available)
            available.remove(finished_task)
            current_tasks[worker_data] = None


def get_next_available_step(available, current_tasks):
    next_steps = choose_x_available(available, 1, current_tasks)
    return next_steps[0] if len(next_steps) > 0 else None


def get_parallel_steps(nodes, workers=5):
    available = [nodes[node] for node in nodes if len(nodes[node].parents) == 0]
    steps = []
    time = 0
    workers_times = {worker: 0 for worker in range(1, workers + 1)}
    current_tasks = {worker: None for worker in range(1, workers + 1)}
    while len(available) > 0 or any(current_tasks.values()):
        check_any_finished_tasks(current_tasks, workers_times, time, steps, available)
        next_step = get_next_available_step(available, current_tasks)
        if not next_step:
            time += 1
            continue
        assigned = False
        while not assigned:
            check_any_finished_tasks(current_tasks, workers_times, time, steps, available)
            for worker in workers_times:
                his_time = workers_times[worker]
                if his_time <= time:
                    workers_times[worker] = time + get_step_length(next_step.value)
                    assigned = True
                    current_tasks[worker] = next_step
                    break
            if not assigned:
                time += 1
        # by this time task should be assigned
    answer = max(workers_times.values())
    print("Answer to part 2:", answer)
    assert(985 == answer)


def get_index_from_letter(letter):
    return ord(letter) - 64


def get_step_length(value):
    return 60 + get_index_from_letter(value)


def choose_next_from_available(nodes):
    return min(nodes, key=attrgetter('value'))


if __name__ == "__main__":
    tests()
    main()
