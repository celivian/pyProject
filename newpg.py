import pygame
import copy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 18

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, sc):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(sc, 'green' if self.board[y][x] else 'black',
                                 [self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size])
                pygame.draw.rect(sc, (255, 255, 255), [self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                       self.cell_size, self.cell_size], 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
        return cell

    def get_cell(self, pos):
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:
            a = (x, y, self.board[y][x])
            return a

    def on_click(self, coord):
        self.board[coord[1]][coord[0]] = not (self.board[coord[1]][coord[0]])


class Life(Board):
    def __init__(self):
        super().__init__(30, 30)

    def next_move(self):
        self.tempboard = copy.deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                summ = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx + x < 0 or dy + y < 0 or dx + x >= self.width or dy + y >= self.height:
                            continue
                        summ += self.board[y + dy][x + dx]
                summ -= self.board[y][x]
                if summ == 3:
                    self.tempboard[y][x] = 1
                if summ < 2 or[y + dy] summ > 3:
                    self.tempboard[y][x] = 0
                self.board = self.tempboard.copy()


flag = 0
speed = 0
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
board = Life()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                speed += 1
            if event.button == 5:
                speed += 1


            print(board.get_click(event.pos))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag = not (flag)

    if flag:
        board.next_move()

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
