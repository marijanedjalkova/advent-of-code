import unittest
from one import is_ok, is_ok_2


class TestMethods(unittest.TestCase):

    def test_1_pt1(self):
        self.assertEqual(True, is_ok("111111", True))

    def test_2_pt1(self):
        self.assertEqual(False, is_ok("223450", True))

    def test_3_pt1(self):
        self.assertEqual(False, is_ok("123789", True))

    def test_1_pt2(self):
        self.assertEqual(True, is_ok_2("112233", True))

    def test_2_pt2(self):
        self.assertEqual(False, is_ok_2("123444", True))

    def test_3_pt2(self):
        self.assertEqual(True, is_ok_2("111122", True))
