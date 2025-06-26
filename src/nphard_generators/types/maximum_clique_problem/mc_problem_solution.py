"""Contains a class representing a maximum-clique-problem with known maximum-clique.

Typical usage example:

    problem = MCProblemSolution(graph, [0,1,2]) # Maximum-clique are nodes 0,1 and 2
    problem.to_file(path, [])
"""

__all__ = [
    "assert_is_np_int_array",
    "assert_is_subset",
    "get_np_array_incremented",
    "get_np_array_as_string",
    "MCProblemSolution"
]

import numpy as np
from scipy.sparse import csr_array

from nphard_generators.types import MCProblemSimpleSolution


def assert_is_np_int_array(arr: np.ndarray) -> bool:
    """Raises ValueError if the array is not a 1D numpy int array."""

    if not isinstance(arr, np.ndarray):
        raise ValueError(f"Array must be a numpy array. Found {type(arr)}.")

    if not arr.ndim == 1:
        raise ValueError(f"Array must be one dimensional. Found {arr.ndim} dimensions.")

    if not np.issubdtype(arr.dtype, np.integer):
        raise ValueError(f"Array must contain integers. Found {arr.dtype}.")


def assert_is_subset(subset: np.ndarray, superset: np.ndarray) -> bool:
    """Raises ValueError if the subset array is not a subset of the superset array."""

    if not all(node in superset for node in subset):
        raise ValueError(f"Given subset {subset} not a subset of {superset}.")


def get_np_array_incremented(arr: np.ndarray, increment: int):
    """Increments each value in arr by increment and returns an incremented copy."""
    arr_incremented = arr.copy()
    arr_incremented += increment
    return arr_incremented


def get_np_array_as_string(arr: np.ndarray):
    """Converts [1,2,3] to "[1,2,3]"."""
    return np.array2string(arr,separator=',',max_line_width=np.inf).replace(' ','')



class MCProblemSolution(MCProblemSimpleSolution):
    """Represents a maximum-clique-problem with known maximum-clique.
    
    to_file(...) stores the problem and maximum-clique in mtx format.
    """

    def __init__(self, graph: csr_array, max_clique: np.ndarray):
        super().__init__(graph, max_clique.size)

        assert_is_np_int_array(max_clique)
        assert_is_subset(max_clique, self.available_verticies)

        self._max_clique = max_clique

    @property
    def max_clique(self):
        """Maximum-clique of the instance.
        Represented as numpy array of nodes.
        E.g.: max_clique = [0,1,2]"""
        return self._max_clique

    def to_file(self, path_to_file: str, comments: list[str] = None):

        max_clique_comment = f"max_clique: {get_np_array_as_string(self.max_clique)}"

        super().to_file(path_to_file, [max_clique_comment] + comments)
