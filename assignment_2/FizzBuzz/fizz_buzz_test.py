__author__ = 'alexmcneill'
import unittest
from fizz_buzz import check_buzz, check_fizz, get_fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_fizz(self):
        self.assertEqual(False, check_fizz(1))
        self.assertEqual(True, check_fizz(3))
        self.assertEqual(False, check_fizz(5))
        self.assertEqual(True, check_fizz(6))
        self.assertEqual(False, check_fizz(10))
        self.assertEqual(True, check_fizz(15))

    def test_check_buzz(self):
        self.assertEqual(False, check_buzz(1))
        self.assertEqual(False, check_buzz(3))
        self.assertEqual(True, check_buzz(5))
        self.assertEqual(False, check_buzz(6))
        self.assertEqual(True, check_buzz(10))
        self.assertEqual(True, check_buzz(15))

    def test_get_fizz_buzz(self):
        self.assertEqual("1", get_fizz_buzz(1))
        self.assertEqual("Fizz", get_fizz_buzz(3))
        self.assertEqual("Buzz", get_fizz_buzz(5))
        self.assertEqual("Fizz", get_fizz_buzz(6))
        self.assertEqual("Buzz", get_fizz_buzz(10))
        self.assertEqual("FizzBuzz", get_fizz_buzz(15))

if __name__ == '__main__':
    unittest.main()