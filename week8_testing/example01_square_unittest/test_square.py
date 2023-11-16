import unittest

from square import square

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)