import unittest
from one import run_program


class TestMethods(unittest.TestCase):

    def test_1_pt1(self):
        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
                         run_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]))

    def test_2_pt1(self):
        self.assertEqual([2, 0, 0, 0, 99], run_program([1, 0, 0, 0, 99]))

    def test_3_pt1(self):
        self.assertEqual([2, 3, 0, 6, 99], run_program([2, 3, 0, 3, 99]))

    def test_4_pt1(self):
        self.assertEqual([2, 4, 4, 5, 99, 9801], run_program([2, 4, 4, 5, 99, 0]))

    def test_5_pt1(self):
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]))


if __name__ == '__main__':
    unittest.main()
