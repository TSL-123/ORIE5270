import unittest
from bellman_ford import find_negative_cicles


class Test_Negative_Cycles(unittest.TestCase):
    def test_1(self):
        assert find_negative_cicles("bellman_ford_1.txt") is None

    def test_2(self):
        assert find_negative_cicles("bellman_ford_2.txt") == [8, 5, 7, 8]
