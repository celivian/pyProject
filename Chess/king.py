WHITE = 1
BLACK = 2


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class King:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'K'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        b = board
        if not correct_coords(row, col):
            return False
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col and not (abs(self.row - row) == abs(self.col - col)):
            return False
        if not abs(self.row - row) <= 1 or not abs(self.col - col) <= 1:
            return False
        if board[row][col]:
            return False

        return True
