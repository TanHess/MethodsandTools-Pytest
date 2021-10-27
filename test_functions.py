from decimal import DivisionByZero
import pytest
from functions import *

def test_numbers_ints():
    assert numbers(18,9) == 2

def test_numbers_floats():
    assert numbers(2.6, 1.6) == 1.625

def test_numbers_strings():
    with pytest.raises(TypeError):
        numbers("hello", "world")

def test_numbers_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        numbers(5, 0)

def test_numbers_fail():
    assert numbers(6, 3) == 5

