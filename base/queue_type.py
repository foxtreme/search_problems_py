from enum import Enum


class QueueType(Enum):
    PRIORITY = "priority"
    FIFO = "fifo"
    LIFO = "lifo"
