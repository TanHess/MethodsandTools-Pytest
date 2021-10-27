from _pytest import capture
import pytest
from functions import *


# Original function returns nothing and outputs 'File opened.'
# To test this, we test the function == True, and test the output with capture_stderr
@pytest.mark.parametrize('test_file', ['testing.txt', 52020, 'fake_file_haha.txt'])
def test_openFile(test_file, capsys):
    if openFile(test_file) == True:
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == 'File opened.'
    else:
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == 'Unexpected error!'

# Original function is supposed to calculate the distance between two points. 
# To test this, test ints, floats, and invalid input (string in ths case).
# Also test combination of these methods
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
