"""Generates a Maximum-Clique-Problem using the hamming distance.

A graph is always represented as a square (sparse) matrix.

Usage:
    problem = MCPHamming2Factory.generate_instance(...)
"""

__all__ = [
    "MCPHamming2Factory"
]


from math import ceil, floor, log2

import numpy as np
from nphard_generators.graph_factory import GraphFactory
from nphard_generators.types.maximum_clique_problem.mc_problem_solution import MCProblemSolution


class MCPHamming2Factory(GraphFactory):
    """Generates graphs for the maximum-clique-problem using the hamming distance.

    Implements the algorithm described by Hasselberg et al. (1993) for generating
    test cases using the hamming distance.

    Edges are always connect when they have a hamming distance of 2 (or more),
    since it is unclear, if the maximum clique is always known for a distance > 2.

    Usage:

        For a Hamming2 graph with 20 nodes:
        MCPHamming2Factory.generateInstance(20)

    References:
        Hasselberg, J., Pardalos, P. M., & Vairaktarakis, G. (1993).
        Test case generators and computational results for the maximum clique problem.
        *Journal of Global Optimization, 3*, 463-482.
    """

    @staticmethod
    # pylint: disable=arguments-differ
    def generate_instance(n_nodes: int) -> MCProblemSolution:
        """Creates a MaxCliqueProblem using the hamming distance."""
        return MCPHamming2Factory(n_nodes).connect_graph().to_problem()

    def __init__(self, n_nodes: int):
        super().__init__(n_nodes)

        self._max_clique = self._calculate_max_clique()

    def to_problem(self) -> MCProblemSolution:
        """Creates a MCProblemSolution out of this factory."""
        return MCProblemSolution(self._get_final_graph(), self._max_clique)

    def _connect_graph_logic(self):
        """Connects the graph using the hamming distance."""

        for vert1 in range(0, self.n_nodes-1):
            for vert2 in range(vert1+1, self.n_nodes):
                dist = self._calculate_hamming_distance(vert1, vert2)

                if dist >= 2:
                    self._connect_edge(vert1, vert2)

    def _calculate_hamming_distance(self, a: int, b: int):
        """Calculates the hamming distance of a and b for word_size bits"""
        word_size = ceil(log2(max(a, b)+1))   # +1 because counting starts with 0
        dist = 0

        for pos in range(0, word_size):
            if floor(a / 2**pos)%2 != floor(b/2**pos)%2:
                dist += 1

        return dist

    def _calculate_max_clique(self):
        """Calculates the max clique that is either the group
        that has an odd amount of 1s in its binary representation or
        the one that has an even amout."""
        odd_clique = []
        even_clique = []

        for node in range(self.n_nodes):
            if bin(node).count('1')%2==0:
                even_clique.append(node)
            else:
                odd_clique.append(node)

        if len(even_clique) <= 0:
            even_clique.append(0)

        if len(even_clique) >= len(odd_clique):
            return np.array(even_clique)

        return np.array(odd_clique)
