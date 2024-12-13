import unittest
from addNum import addNumber
#updated numbers
class testFunc(unittest.TestCase):

    def test_positve(self):
       result = addNumber(3, 3)
       self.assertEqual(result, 6)

    def test_negative(self):
        result = addNumber(1, 1)
        self.assertEqual(result, 2)
if __name__ == '__main__':
    unittest.main()