from base.evaluation_function import EvaluationFunction
from base.failure import Failure
from base.node import Node
from base.problem import Problem
from base.queue_type import PriorityQueue
from base.search_method import SearchMethod


class BestFirstSearch(SearchMethod):
    """Returns a solution node or failure using best-first search"""

    def search(self, problem: Problem, eval_function: EvaluationFunction):
        node = Node(state=problem.initial_state)
        frontier = PriorityQueue(eval_function)
        frontier.insert(node)
        reached = {problem.initial_state: node}

        while not frontier.is_empty():
            node = frontier.pop()
            if problem.is_goal(node.state):
                return node
            for child in self.expand(problem, node):
                state = child.state
                if state not in reached or child.path_cost < reached[state].path_cost:
                    reached[state] = child
                    frontier.insert(child)
        raise Failure("A Solution could not be found")

    def expand(self, problem: Problem, node: Node) -> list:
        state = node.state
        for action in problem.actions(state):
            next_state = problem.result(state, action)
            cost = node.path_cost + problem.calculate_cost(state, action, next_state)
            yield Node(state=next_state, parent=node, action=action, path_cost=cost)

