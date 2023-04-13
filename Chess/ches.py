from che import *

board = Board()
if board.move_piece(0, 1, 2, 2):
    print(board)
else:
    print('Error')