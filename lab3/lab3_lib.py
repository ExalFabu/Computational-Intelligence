# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free for personal or classroom use; see 'LICENSE.md' for details.

from abc import abstractmethod
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
class AbstractProblem:
    def __init__(self):
        self._calls = 0

    @property
    @abstractmethod
    def x(self):
        pass

    @property
    def calls(self):
        return self._calls

    @staticmethod
    def onemax(genome):
        return sum(bool(g) for g in genome)

    def __call__(self, genome):
        self._calls += 1
        fitnesses = sorted((AbstractProblem.onemax(genome[s::self.x]) for s in range(self.x)), reverse=True)
        val = fitnesses[0] - sum(f*(.1 ** (k+1)) for k, f in enumerate(fitnesses[1:]))
        fitness = val / len(genome) * self.x
        print(f"{val=} {fitnesses=} {fitness=}")
        
        return fitness

def make_problem(a: int):
    class Problem(AbstractProblem):
        @property
        @abstractmethod
        def x(self):
            return a

    return Problem()
