from nphard_generators.example import FourGenerator

def test_four_generator():
    g = FourGenerator()
    assert g.generate() == 4, "FourGenerator should generate a 4"