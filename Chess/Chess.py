WHITE = 1
BLACK = 2


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


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


class Bishop:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        r = row
        c = col
        if not correct_coords(row, col):
            return False
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if not (abs(self.row - row) == abs(self.col - col)):
            return False
        while r != self.row and c != self.col:
            if board[r][c]:
                return False
            print(board[r][c])
            r -= 1
            c -= 1
        return True


class Knight:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if not correct_coords(row, col):
            return False
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if not (abs(self.row - row) == 1 and abs(self.col - col) == 2 or abs(self.row - row) == 2 and abs(
                self.col - col) == 1):
            return False
        if board[row][col]:
            return False

        return True


class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):
        if not correct_coords(row, col):
            return False
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if self.col != col:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if board[row][col]:
            return False

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


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


class Rook:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, row, col, board):

        r = row
        c = col
        if not correct_coords(row, col):
            return False
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False
        if self.row == row:
            while c != self.col:
                if board[r][c]:
                    return False
                c -= 1
        if self.col == col:
            while r != self.row:
                if board[r][c]:
                    return False
                r -= 1

        return True


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = [[Rook(0, 0, WHITE), Knight(0, 1, WHITE), Bishop(0, 2, WHITE), Queen(0, 3, WHITE),
                       King(0, 4, WHITE), Bishop(0, 5, WHITE), Knight(0, 6, WHITE), Rook(0, 7, WHITE)],
                      [Pawn(1, 0, WHITE), Pawn(1, 1, WHITE), Pawn(1, 2, WHITE), Pawn(1, 3, WHITE),
                       Pawn(1, 4, WHITE), Pawn(1, 5, WHITE), Pawn(1, 6, WHITE), Pawn(1, 7, WHITE)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(6, 0, BLACK), Pawn(6, 1, BLACK), Pawn(6, 2, BLACK), Pawn(6, 3, BLACK),
                       Pawn(6, 4, BLACK), Pawn(6, 5, BLACK), Pawn(6, 6, BLACK), Pawn(6, 7, BLACK)],
                      [Rook(7, 0, BLACK), Knight(7, 1, BLACK), Bishop(7, 2, BLACK), Queen(7, 3, BLACK),
                       King(7, 4, BLACK), Bishop(7, 5, BLACK), Knight(7, 6, BLACK), Rook(7, 7, BLACK)
                       ]]
        for row in range(8):
            self.field.append([None] * 8)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1, self.field):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in self.field:
            for j in i:
                if j:
                    if j.can_move(row, col, self.field) and j.get_color() == color:
                        return True


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


if __name__ == '__main__':
    main()
