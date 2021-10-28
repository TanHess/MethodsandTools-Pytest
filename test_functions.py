from _pytest import capture
from decimal import DivisionByZero
import pytest
from functions import *

'''=======================FUNCTION 1======================='''
# Original function returns nothing and outputs 'File opened.'
# To test this, we test the function == True, and test the output with capture_stderr
# TOTAL: 3 TESTS
@pytest.mark.parametrize('test_file', ['testing.txt', 52020, 'fake_file_haha.txt'])
def test_openFile(test_file, capsys):
    if openFile(test_file) == True:
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == 'File opened.'
    else:
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == 'Unexpected error!'


'''=======================FUNCTION 2======================='''
def test_numbers_ints():
    assert numbers(18,9) == 2

def test_numbers_floats():
    assert numbers(2.6, 1.6) == 1.625

def test_numbers_strings():
    assert numbers("hello", "world") == "Error: Can't divide with strings"

def test_numbers_divide_by_zero():
    assert numbers(5, 0) == "Error: Divide by Zero"

def test_numbers_fail():
    assert numbers(6, 3) == 5


'''=======================FUNCTION 3======================='''
# Original function is supposed to calculate the distance between two points. 
# To test this, test ints, floats, and invalid input (string in ths case).
# Also test combination of these methods. TOTAL: 5 TESTS
@pytest.mark.parametrize('x1, y1, x2, y2', [(2, 2, 3, 2), (1.5, 1.5, 2.5, 1.5),\
                                            ('Hello!', 'this', "won't", 'work!' ), (2, 2, 'hi', 2),\
                                             ('1', 2, '1', 1)])
def test_dist(x1, y1, x2, y2):
    if x1 == 'Hello!':
        assert dist(x1, y1, x2, y2) == False
    elif x2 == 'hi':
        assert dist(x1, y1, x2, y2) == False
    else:
        assert dist(x1, y1, x2, y2) == 1

'''=======================FUNCTION 4======================='''
@pytest.mark.parametrize('value', ['string', 'racecar', True, 54])
def test_isPalindrome(value):
    if value == 'string':
        assert isPalindrome(value) == False
    elif value == 'racecar':
        assert isPalindrome(value) == True
    elif value == True:
        assert isPalindrome(value) == "Invalid"
    elif value == 54:
        assert isPalindrome(value) == "Invalid"

'''=======================FUNCTION 5======================='''
def division_inputs1(spec):
    if spec == 1:
        inputs = [1, 2]
    elif spec == 2:
        inputs =[2, 4]
    elif spec == 3:
        inputs = ['Will', 'this work']
    elif spec == 4:
        inputs = [4, 0]
    for item in inputs:
        yield item

# First test, valid inputs, should return .5
def test_divide1(monkeypatch, capsys):
    input = division_inputs1(1)
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 0.5"

# Second test, once again valid inputs, should return 0.5
def test_divide2(monkeypatch, capsys):
    input = division_inputs1(2)
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your numbers divided is: 0.5"

# Third test, invalid inputs (strings), should fail.
def test_divide3(monkeypatch, capsys):
    input = division_inputs1(3)
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error! Only numbers and no division by zero!"

# 4th and final test. Division by 0, should fail.
def test_divide4(monkeypatch, capsys):
    input = division_inputs1(4)
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error! Only numbers and no division by zero!"

