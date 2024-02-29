import pygame
import random as rr


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, name_screen):
        for x in range(0, self.width):
            for y in range(0, self.height):
                pygame.draw.rect(name_screen, 'white', (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                        self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        # self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            print((x, y))
        else:
            print(None)


class Minesweeper(Board):
    def __init__(self, rows, cols, bombs):
        super().__init__(rows, cols)
        self.board = [[-1] * rows for _ in range(cols)]
        for i in range(bombs):
            self.board[rr.randint(0, cols - 1)][rr.randint(0, rows - 1)] = 10

    def render(self, screen):
        for x in range(0, self.width):
            for y in range(0, self.height):
                pygame.draw.rect(screen, 'red' if self.board[y][x] == 10 else "black", (
                    self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, 'white', (
                    self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size), 1)
                if 0 <= self.board[y][x] <= 8:
                    f1 = pygame.font.Font(None, self.cell_size // 2)
                    text1 = f1.render(str(self.board[y][x]), True, (0, 255, 0))
                    screen.blit(text1, (self.left + x * self.cell_size + 3, self.top + y * self.cell_size + 3))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.open_cell(cell)

    def open_cell(self, cell):
        if self.board[cell[1]][cell[0]] == -1:
            bombs = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx + cell[0] < 0 or dy + cell[1] < 0 or dx + cell[0] >= self.width or dy + cell[
                        1] >= self.height:
                        continue
                    if self.board[cell[1] + dy][cell[0] + dx] == 10:
                        bombs += 1
            self.board[cell[1]][cell[0]] = bombs

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            return (x, y)
        else:
            return None


if __name__ == '__main__':
    pygame.font.init()
    board = Minesweeper(10, 15, 10)
    running = True
    screen = pygame.display.set_mode([500, 500])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
