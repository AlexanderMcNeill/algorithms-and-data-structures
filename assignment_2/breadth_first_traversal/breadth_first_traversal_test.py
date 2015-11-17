__author__ = 'alexmcneill'
import unittest
import breadth_first_traversal
import tree


class TestBreadthFirst(unittest.TestCase):

    def setUp(self):
        pass

    def test_breadth_first_traversal(self):
        t = tree.BasicTree()
        t.put(5, 5)
        t.put(8, 8)
        t.put(3, 3)
        t.put(19, 19)
        t.put(1, 1)
        t.put(4, 4)

        result = breadth_first_traversal.create_breadth_first_traversal_list(t)

        self.assertEqual([5, 3, 8, 1, 4, 19], result)

if __name__ == '__main__':
    unittest.main()