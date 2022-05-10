from abc import ABC


class Node(ABC):

    def __init__(self, state, parent=None, action=None, path_cost=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
