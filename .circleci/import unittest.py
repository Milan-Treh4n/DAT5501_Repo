import unittest
from Function_for_unit_test import milan_function

def test_milan_function():
    assert milan_function(2, 3) == 5
    assert milan_function(-1, 1) == 0