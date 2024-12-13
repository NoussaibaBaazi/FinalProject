import unittest
from addNum import addNumber
#new edit
class testFunc(unittest.TestCase):

    def test_positve(self):
       result = addNumber(3, 8)
       self.assertEqual(result, 3)

    def test_negative(self):
        result = addNumber(-34, -17)
        self.assertEqual(result, -34)
if __name__ == '__main__':
    unittest.main()