from abc import ABC, abstractmethod


class Frontier(ABC):

    @abstractmethod
    def __init__(self, kwargs):
        ...

    @abstractmethod
    def is_empty(self):
        ...

    @abstractmethod
    def insert(self, element):
        ...

    @abstractmethod
    def pop(self):
        ...

