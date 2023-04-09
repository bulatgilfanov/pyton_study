import pygame

size = input("Введите 2 числа через пробел:")
size = size.split()
n, a = int(size[0]), int(size[1])
rect = n // a



pygame.init()
win = pygame.display.set_mode((n, n))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255, 255, 255)
    win.fill(color)
    for i in range(a):
        for j in range(a):
            if (i + j) % 2 == 0:
                pygame.draw.rect(win, (0, 255, 0), (i * rect, j * rect, (i+1) * rect, (j+1) * rect))
                pygame.display.update()

    pygame.display.update()