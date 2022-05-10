from abc import ABC, abstractmethod


class Problem(ABC):
    """An atomic abstraction of a problem"""
    
    @property
    @abstractmethod
    def initial_state(self):
        ...

    @abstractmethod
    def actions(self, state):
        ...

    @abstractmethod
    def is_goal(self, state):
        ...

    @abstractmethod
    def result(self, state, action):
        ...

    @abstractmethod
    def calculate_cost(self, state, action, next_state):
        ...


