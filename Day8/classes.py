class Node:

    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)

    def get_metadata_sum(self):
        return sum(self.metadata)
