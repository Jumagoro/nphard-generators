"""Simple sandbox. Can be overwritten any time"""


import numpy as np
from scipy.sparse import csr_array

#from nphard_generators.types import MCProblemSolution
from nphard_generators.types.maximum_clique_problem.mc_problem_simple_solution import MCProblemSimpleSolution


row = np.array([0, 1, 0, 2, 1, 2])
col = np.array([1, 0, 2, 0, 2, 1])
data = np.ones(len(row), dtype=bool)
graph = csr_array((data, (row, col)), shape=(3, 3))

mc_problem_solution = MCProblemSimpleSolution(graph, 3)