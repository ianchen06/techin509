import pytest

from app import Game

def test_switch_player():
    g = Game(player1='O', player2='X') # Doesn't even need to be a HumanPlayer or BotPlayer, here we just use strings as players
    g.switch_player()
    assert g.current_player == 'X'