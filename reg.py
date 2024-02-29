import pygame

size1 = input()
n = int(size1.split()[0])
k = int(size1.split()[1])

sz = n * k * 2

pygame.init()
size = width, height = sz, sz
screen = pygame.display.set_mode(size)
color = pygame.Color(255, 255, 255)
c = 0
for i in range(k):
    pygame.draw.ellipse(screen, color, (0, 0), width=k)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()
