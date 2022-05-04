from abc import ABC, abstractmethod


class Frontier(ABC):

    @abstractmethod
    def __init__(self, queue_type):
        ...
