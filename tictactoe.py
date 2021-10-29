import sys

human = 'X'
ai = 'O'
max_int = sys.maxsize
min_int = -sys.maxsize - 1

class Move:
    def __init__(self, row, col):
        self.row=row # instance attribute
        self.col=col

def checkWinner(board):
    # check rows
    for row in range(3):
        if (board[row][0] == board[row][1]) and (board[row][1] == board[row][2]):
            if board[row][0] == human:
                return 1
            elif board[row][0] == ai:
                return -1
