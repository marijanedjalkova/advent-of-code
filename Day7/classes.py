class Node:

    def __init__(self, value):
        self.value = value
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return False
