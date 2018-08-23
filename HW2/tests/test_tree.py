import unittest
from Tree.Elliot_HW2 import Tree, Node

class TestTree(unittest.TestCase):
	def test_1(self):
# a one leg tree
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
		k = Node(11, e,f)
		l = Node(12, g, h)
		m = Node(13, i,j)
		n = Node(14, k,l)
		o = Node(15, m, None)
		tree=Tree(o)
		assert Tree.print_tree(tree) == [['|', '|', '|', '|', '|', '|', '|', 15, '|', '|', '|', '|', '|', '|', '|'], ['|', '|', '|', 13, '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'], ['|', 9, '|', '|', '|', 10, '|', '|', '|', '|', '|', '|', '|', '|', '|'], [1, '|', 2, '|', 3, '|', 4, '|', '|', '|', '|', '|', '|', '|', '|']]
