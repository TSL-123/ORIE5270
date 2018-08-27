import unittest
from dijkstra import find_shortest_path


class Test_shortest_path(unittest.TestCase):
    def test_1(self):
        assert find_shortest_path("dijkstra_1.txt", 1, 4) == (3, [1, 2, 4])

    def test_2(self):
        assert find_shortest_path("dijkstra_2.txt", 1, 8) == (5, [1, 3, 6, 5, 7, 8])