from app import add

def test_addition():
    assert add(10, 20) == 30

def test_addition_zero():
    assert add(5, 0) == 5