import unittest
from one import run_programs


class TestMethods(unittest.TestCase):

    def test1(self):
        input_stuff = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105," \
                      "1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99 "
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 7, True)
        self.assertEqual(999, int(output))

    def test2(self):
        input_stuff = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105," \
                      "1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99 "
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 8, True)
        self.assertEqual(1000, int(output))

    def test3(self):
        input_stuff = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105," \
                      "1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99 "
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 9, True)
        self.assertEqual(1001, int(output))

    def test4(self):
        input_stuff = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 1, True)
        self.assertEqual(1, int(output))

    def test5(self):
        input_stuff = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 0, True)
        self.assertEqual(0, int(output))
        
    def test6(self):
        input_stuff = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 1, True)
        self.assertEqual(1, int(output))

    def test7(self):
        input_stuff = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
        numbers = input_stuff.split(",")
        output = run_programs(numbers, 0, True)
        self.assertEqual(0, int(output))
