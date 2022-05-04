from abc import ABC, abstractmethod


class EvaluationFunction(ABC):
    """A function that evaluates object according to some criteria"""

    @abstractmethod
    def evaluate(self, obj):
        ...
