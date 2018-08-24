import unittest
from tree.Elliot_HW2 import Tree, Node


class TestTree(unittest.TestCase):
    def test_1(self):
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        i = Node(9, a, b)
        j = Node(10, c, d)
        m = Node(13, i, j)
        o = Node(15, m, None)
        tree = Tree(o)
        self.res = [['|', '|', '|', '|', '|', '|', '|', 15, '|', '|', '|', '|', '|', '|', '|'],
                    ['|', '|', '|', 13, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                    ['|', 9, '|', '|', '|', 10, '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                    [1, '|', 2, '|', 3, '|', 4, '|', '|', '|', '|', '|', '|', '|', '|']]
        assert Tree.print_tree(tree) == self.res

    def test_2(self):
        # a full tree
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        g = Node(7, None, None)
        h = Node(8, None, None)
        i = Node(9, a, b)
        j = Node(10, c, d)
        k = Node(11, e, f)
        ll = Node(12, g, h)
        m = Node(13, i, j)
        n = Node(14, k, ll)
        o = Node(15, m, n)
        tree = Tree(o)
        self.res = [['|', '|', '|', '|', '|', '|', '|', 15, '|', '|', '|', '|', '|', '|', '|'],
                    ['|', '|', '|', 13, '|', '|', '|', '|', '|', '|', '|', 14, '|', '|', '|'],
                    ['|', 9, '|', '|', '|', 10, '|', '|', '|', 11, '|', '|', '|', 12, '|'],
                    [1, '|', 2, '|', 3, '|', 4, '|', 5, '|', 6, '|', 7, '|', 8]]
        assert Tree.print_tree(tree) == self.res

    def test_3(self):
        o = Node(15, None, None)
        tree = Tree(o)
        assert Tree.print_tree(tree) == [[15]]

    def test_4(self):
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        h = Node(8, None, None)
        i = Node(9, None, b)
        j = Node(10, c, d)
        k = Node(11, e, None)
        ll = Node(12, None, h)
        m = Node(13, i, j)
        n = Node(14, k, ll)
        o = Node(15, m, n)
        tree = Tree(o)
        self.res = [['|', '|', '|', '|', '|', '|', '|', 15, '|', '|', '|', '|', '|', '|', '|'],
                    ['|', '|', '|', 13, '|', '|', '|', '|', '|', '|', '|', 14, '|', '|', '|'],
                    ['|', 9, '|', '|', '|', 10, '|', '|', '|', 11, '|', '|', '|', 12, '|'],
                    ['|', '|', 2, '|', 3, '|', 4, '|', 5, '|', '|', '|', '|', '|', 8]]
        assert Tree.print_tree(tree) == self.res
