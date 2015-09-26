__author__ = 'alexmcneill'


import unittest
from spell_checker import SpellChecker, CachedMistake

class TestSpellChecker(unittest.TestCase):

    def test_check_swapped_characters(self):
        self.assertEqual(SpellChecker.check_swapped_characters("dad", "add"), True)
        self.assertEqual(SpellChecker.check_swapped_characters("dadd", "add"), False)

    def test_check_missing_character(self):
        self.assertEqual(SpellChecker.check_missing_character("dd", "add"), True)
        self.assertEqual(SpellChecker.check_missing_character("ddd", "add"), False)
        self.assertEqual(SpellChecker.check_missing_character("hd", "add"), False)

    def test_check_incorrect_character(self):
        self.assertEqual(SpellChecker.check_incorrect_character("agd", "add"), True)
        self.assertEqual(SpellChecker.check_incorrect_character("gd", "add"), False)


if __name__ == '__main__':
    unittest.main()
