"""Tests a HCProblem instance"""
import pytest

import numpy as np
import numpy.testing as npt


from nphard_generators import MCPHamming2Factory
from nphard_generators.types import MCProblemSolution


class TestMCPRandomFactory:
    """Tests for the MCPHamming2Factory."""

    @pytest.mark.parametrize("n, max_clique_expected", [
        (9, np.array([1,2,4,7,8])),
        (10, np.array([0,3,5,6,9])),
    ])
    def test_various_shapes(self, n, max_clique_expected):
        """Test some configurations for expected max_clique"""
        hamming_problem = MCPHamming2Factory.generate_instance(n)

        assert isinstance(hamming_problem, MCProblemSolution)
        assert hamming_problem.n_nodes == n, "n_nodes differs."

        npt.assert_array_equal(
            hamming_problem.max_clique, max_clique_expected, "max_clique differs from expected."
        )
