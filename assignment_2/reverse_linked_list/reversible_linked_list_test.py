__author__ = 'alexmcneill'

import unittest
from reversible_linked_list import ReversibleLinkedList


class TestReverseLinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def test_reverse_list(self):
        l = ReversibleLinkedList()
        l.reverse_list()
        self.assertEqual("[]", str(list))

        l.enqueue(8)
        l.reverse_list()
        self.assertEqual("[8]", str(list))

        l.enqueue(6)
        l.enqueue(3)
        l.enqueue(8)
        l.enqueue(2)
        l.enqueue(81)
        l.enqueue(11)
        l.reverse_list()
        self.assertEqual("[11, 81, 2, 8, 3, 6, 8]", str(list))

if __name__ == '__main__':
    unittest.main()