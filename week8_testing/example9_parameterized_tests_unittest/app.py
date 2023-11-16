class OutOfBoundsError(Exception):
    pass

class SpaceAlreadyTaken(Exception):
    pass

class Board:
    def __init__(self) -> None:
        self.board = [' ' for x in range(9)]
    
    def place_symbol(self, move, symbol):
        if move >= len(self.board):
            raise OutOfBoundsError("move out of bounds")
        if self.board[move] != " ":
            raise SpaceAlreadyTaken("move already taken")
        self.board[move] = symbol