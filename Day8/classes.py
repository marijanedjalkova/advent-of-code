class Node:

    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)

    def get_metadata_sum(self):
        return sum(self.metadata)

    def get_value(self):
        if not self.children:
            return self.get_metadata_sum()
        values = [self.children[index-1].get_value() for index in self.metadata if 0 < index <= len(self.children)]
        return sum(values)

