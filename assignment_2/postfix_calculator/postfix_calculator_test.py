__author__ = 'alexmcneill'

import unittest
from postfix_calculator import calculate


class TestPostfixCalc(unittest.TestCase):

    def setUp(self):
        pass

    def test_calculate(self):
        self.assertEqual(3, calculate("1 2 +"))
        self.assertEqual(-1, calculate("1 2 -"))
        self.assertEqual(2, calculate("1 2 *"))
        self.assertEqual(.5, calculate("1 2 /"))
        self.assertEqual(1, calculate("1 2 %"))
        self.assertEqual(1, calculate("3 2 %"))
        self.assertEqual(6, calculate("1 2 + 2 *"))

if __name__ == '__main__':
    unittest.main()