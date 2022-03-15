class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, node):
        self.next = node
