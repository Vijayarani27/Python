from TestDemo import multiply

def test_mul():
    assert multiply(2,4) == 8

def test_mul_with_zero():
    assert multiply(0,4) == 0    