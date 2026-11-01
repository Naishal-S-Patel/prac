import pytest

@pytest.fixture
def input_value():
    return 100

@pytest.mark.great
def test_greater(input_value):
    num=input_value
    assert num>50

def test_greater_equal():
    num=100
    assert num>=100

def test_less():
    num=100
    assert num<50