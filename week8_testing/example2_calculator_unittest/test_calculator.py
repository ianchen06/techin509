import unittest

from calculator import Calculator

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 1), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5,1), 4)

    def test_multiply(self):
        pass

    def test_divide(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(2,0)