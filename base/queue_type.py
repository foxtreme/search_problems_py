from enum import Enum

from base.frontier import Frontier


class QueueType(Enum):
    PRIORITY = "priority"
    FIFO = "fifo"
    LIFO = "lifo"


class PriorityQueue(Frontier):

    def __init__(self, eval_function):
        self.queue = []
        self.eval_function = eval_function

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, element):
        self.queue.append(element)

    def pop(self):
        if not self.is_empty():
            min_val = self.eval_function(self.queue[0])
            for element in range(2, len(self.queue)+1):
                min_val = min_val if min_val < self.eval_function(element) else self.eval_function(element)
            return min_val
        return None
