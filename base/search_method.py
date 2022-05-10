from abc import ABC, abstractmethod


class SearchMethod(ABC):

    @abstractmethod
    def search(self, **kwargs):
        ...

    @abstractmethod
    def expand(self, **kwargs):
        ...
