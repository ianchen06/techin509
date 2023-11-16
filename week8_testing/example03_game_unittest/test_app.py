import unittest

from app import Game

class TestGame(unittest.TestCase):
    def test_switch_player(self):
        g = Game(player1='O', player2='X') # Doesn't even need to be a HumanPlayer or BotPlayer, here we just use strings as players
        g.switch_player()
        self.assertEqual(g.current_player, 'X')