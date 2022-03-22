from rtd.calculator.operations import add, multiply, subtract


def test_add():
    assert add(1, 5) == 6
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(5, 5) == 25

def test_subtract():
    assert subtract(20, 5) == 15
