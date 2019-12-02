import unittest
from one import get_mass
from two import get_mass_with_fuel


class TestMethods(unittest.TestCase):

    def test_12(self):
        self.assertEqual(2, get_mass(12))

    def test_14(self):
        self.assertEqual(2, get_mass(14))

    def test_1969(self):
        self.assertEqual(654, get_mass(1969))

    def test_100756(self):
        self.assertEqual(33583, get_mass(100756))

    def test_14_with_fuel(self):
        self.assertEqual(2, get_mass_with_fuel(14))

    def test_1969_with_fuel(self):
        self.assertEqual(966, get_mass_with_fuel(1969))

    def test_100756_with_fuel(self):
        self.assertEqual(50346, get_mass_with_fuel(100756))


if __name__ == '__main__':
    unittest.main()
