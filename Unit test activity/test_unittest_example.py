import unittest
from Milan_function import milan_function

class TestMilanFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(milan_function(6, 7), 13)
        self.assertEqual(milan_function(3.5, 2.5), 6.0)
        

if __name__ == '__main__':
    unittest.main()