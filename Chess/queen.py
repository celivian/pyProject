WHITE = 1
BLACK = 2


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Queen:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        r = row
        c = col
        if not correct_coords(row, col):
            return False
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col and not (abs(self.row - row) == abs(self.col - col)):
            return False

        if self.row != row and self.col != col:
            r = row - 1
            c = col - 1
            while r != self.row and c != self.col:
                if board[r][c]:
                    return False
                print(board[r][c])
                r -= 1
                c -= 1
        if self.row == row and self.col != col:
            while c != self.col:
                if board[r][c]:
                    return False
                c -= 1
        if self.col == col and self.row != row:
            while r != self.row:
                if board[r][c]:
                    return False
                r -= 1

        return True
