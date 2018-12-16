class Node:

    def __init__(self, value):
        self.value = value
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)
