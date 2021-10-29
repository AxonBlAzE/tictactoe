import sys

human = 'X'
ai = 'O'
max_int = sys.maxsize
min_int = -sys.maxsize - 1

class Move:
    def __init__(self, row, col):
        self.row=row
        self.col=col

def checkWinner(board):
    # check rows
    for row in range(3):
        if (board[row][0] == board[row][1]) and (board[row][1] == board[row][2]):
            if board[row][0] == human:
                return 1
            elif board[row][0] == ai:
                return -1
    # check cols
    for col in range(3):
        if (board[0][col] == board[1][col]) and (board[1][col] == board[2][col]):
            if board[0][col] == human:
                return 1
            elif board[0][col] == ai:
                return -1

    # check diagonals    
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        if board[0][0] == human:
            return 1
        elif board[0][0] == ai:
            return -1
    
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        if board[0][2] == human:
            return 1
        elif board[0][2] == ai:
            return -1
    
    return 0

def movesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return True
    return False