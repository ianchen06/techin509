import unittest

from app import Board, OutOfBoundsError, SpaceAlreadyTaken

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_place_symbol(self):
        test_cases = [
            ["out of bounds", 9, True, OutOfBoundsError],
            ["valid move", 1, False, 'X'],
            ["space already taken", 1, True, SpaceAlreadyTaken]
        ]
        for description, move, is_expect_error, expected in test_cases:
            with self.subTest(description, move=move, is_expect_error=is_expect_error, expected=expected):
                if is_expect_error:
                    with self.assertRaises(expected):
                        self.board.place_symbol(move, 'X')
                else:
                    self.board.place_symbol(move, 'X')
                    self.assertEqual(self.board.board[move], expected)
                
                