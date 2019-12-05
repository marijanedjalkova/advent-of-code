import unittest
from one import get_closest_cross


class TestMethods(unittest.TestCase):

    def test_1_pt1(self):
        self.assertEqual(159, get_closest_cross(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
                                                ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]))

    def test_2_pt1(self):
        self.assertEqual(135, get_closest_cross(
            ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
            ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]))

    def test_3_pt1(self):
        self.assertEqual(6, get_closest_cross(
            ["R8", "U5", "L5", "D3"],
            ["U7", "R6", "D4", "L4"]))
