"""Tests a HCProblem instance"""
import pytest

import numpy as np
import numpy.testing as npt


from nphard_generators import MCPCFatFactory
from nphard_generators.types import MCProblemSolution


class TestMCPRandomFactory:
    """Tests for the MCPCFatFactory."""

    @pytest.mark.parametrize("n, c, max_clique_expected", [
        (2, 1, np.array([0,1])),
        (2, 2, np.array([0,1])),
        (10, 0.86, np.array([0,1,5,6])),
        (14, 0.88, np.array([0,1,6,7,12,13])),
    ])
    def test_various_shapes(self, n, c, max_clique_expected):
        """Test some configurations for expected max_clique"""
        cfat_problem = MCPCFatFactory.generate_instance(n, c)

        assert isinstance(cfat_problem, MCProblemSolution)
        assert cfat_problem.n_nodes == n, "n_nodes differs."

        npt.assert_array_equal(
            cfat_problem.max_clique, max_clique_expected, "max_clique differs from expected."
        )


    def test_invalid_c_value(self):
        """If c leads to 0 partition (k), k becomes 1"""
        n=2
        c=3
        cfat_problem = MCPCFatFactory.generate_instance(n, c)
        assert cfat_problem.n_max_clique == n
