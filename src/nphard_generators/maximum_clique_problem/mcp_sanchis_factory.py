"""Generates a Maximum-Clique-Problem using Sanchis graph construction.

A graph is always represented as a square (sparse) matrix.

Usage:
    problem = MCPSanchisFactory.generate_instance(...)
"""

__all__ = [
    "MCPSanchisFactory"
]


from math import floor, log

import numpy as np
from nphard_generators.graph_factory import GraphFactory, assert_density_valid, assert_n_max_clique_valid
from nphard_generators.types.maximum_clique_problem.mc_problem_solution import MCProblemSolution


class MCPSanchisFactory(GraphFactory):
    """Generates graphs for the maximum-clique-problem using the Sanchis algorithm.

    Implements the algorithm described by Hasselberg et al. (1993) for generating
    test cases for the minimum vertex cover problem and converting to
    the maximum clique problem.

    The algorithm is based on an idea orginally proposed by Sanchis (1992) in
    the context of generating NP-hard problems.

    Usage:

        For a Sanchis graph with 20 nodes, density 0.4 and hidden maximum clique of size 4:
        MCPCFatFactory.generateInstance(20, 0.4, 4)

    References:
        Hasselberg, J., Pardalos, P. M., & Vairaktarakis, G. (1993).
        Test case generators and computational results for the maximum clique problem.
        *Journal of Global Optimization, 3*, 463-482.

        Sanchis, L. (1992).
        Test case construction for the vertex cover problem.
        In *DIMACS Series in Discrete Mathematics and Theoretical Computer Science, 15*
        (pp. 315-326). American Mathematical Society.
    """

    @staticmethod
    # pylint: disable=arguments-differ
    def generate_instance(n_nodes: int, density: float, n_max_clique: int) -> MCProblemSolution:
        """Creates a MaxCliqueProblem using the Sanchis generator."""
        return MCPSanchisFactory(n_nodes, density, n_max_clique).connect_graph().to_problem()

    def __init__(self, n_nodes: int, density: float, n_max_clique: int):
        super().__init__(n_nodes)

        assert_density_valid(density)
        self._density = density

        assert_n_max_clique_valid(n_max_clique, n_nodes)
        self._n_max_clique = n_max_clique

        # TODO: Implement
        
        #self._max_clique = self._calculate_max_clique()

    def to_problem(self) -> MCProblemSolution:
        """Creates a MCProblemSolution out of this factory."""
        # TODO: Komplement
        return MCProblemSolution(self._get_final_graph(), self._max_clique)

    def _connect_graph_logic(self):
        """Connects the graph according to the sanchis algorithm.
        """
        # TODO: Implement

    def _calculate_max_clique(self):
        """Calculates the max clique based on ..."""
        # TODO: Implement
