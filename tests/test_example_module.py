

#from nphard_generators.maxclique import BrockGenerator
import numpy as np
import pytest

def test_four_generator():
    a = np.random.random()
    assert isinstance(a, float), "Random number should be float"
    #g = BrockGenerator(200, 0.1).generate()
    #BrockGenerator().generate(200, 0.1)
    #assert g is not None
    #assert g.generate() == 4