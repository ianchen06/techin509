class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1 # make player1 the current player by default

    def switch_player(self):
        next_player = self.player1 if self.current_player == self.player2 else self.player2
        self.current_player = next_player