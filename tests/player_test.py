
import context
import unittest
from life import Life # pylint:disable = import-error

class Test_Neighbors(unittest.TestCase):

    def test_neighbors_is_3_when_top_left_corner(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(0, 0)), 3)


    def test_neighbors_is_5_when_top_edge(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(1, 0)), 5)


    def test_neighbors_is_5_when_left_edge(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(0, 1)), 5)


    def test_neighbors_is_8_when_middle(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(4, 4)), 8)


    def test_neighbors_is_5_when_bottom_edge(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(8, 9)), 5)


    def test_neighbors_is_5_when_right_edge(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(9, 8)), 5)


    def test_neighbors_is_3_when_bottom_right_corner(self):
        scenario = Life()
        self.assertEqual(len(scenario.neighbors(9, 9)), 3)


class Test_Status(unittest.TestCase):

    def test_status_is_alive_when_it_has_3_neighbors(self):
        scenario = Life((3, 3))
        scenario.board[0][0] = '#'
        scenario.board[1][0] = '#'
        scenario.board[0][1] = '#'
        self.assertEqual(scenario.status(1, 1), '#')


if __name__ == '__main__':
    unittest.main()
