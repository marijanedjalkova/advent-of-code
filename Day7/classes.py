class Node:

    def __init__(self, value, parent_node=None, child=None):
        self.value = value
        self.parents = []
        if parent_node is not None:
            self.add_parent(parent_node)
        self.children = []
        if child is not None:
            self.add_child(child)

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child_by_value(self, value):
        self.children.append(Node(value, parent_node=self))

    def add_parent_by_value(self, value):
        self.parents.append(Node(value, child=self))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
            # if self.value != other.value:
            #     return False
            # if len(self.parents) != len(other.parents):
            #     return False
            # if len(self.children) != len(other.children):
            #     return False
            # return not (any([this_child.value != that_child.value for (this_child, that_child) in
            #                  zip(self.children, other.children)])
            #             or any([this_parent.value != that_parent.value for (this_parent, that_parent) in
            #                     zip(self.parents, other.parents)]))
        return False

    def deep_equals(self, other):
        return (self == other) and len(self.children) == len(other.children) and not any(
            [this_child != that_child for (this_child, that_child) in zip(self.children, other.children)])

    # def __repr__(self):
    #     self.children.sort(key=lambda x: x.value)
    #     return "[{}] => {}".format(self.value, self.children[0] if len(self.children) > 0 else "")

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)
