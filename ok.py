import pygame

size = input("Введите 2 числа через пробел:")
size = size.split()
W,H = int(size[0]), int(size[1])

pygame.init()
win = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (0, 0, 0)
    win.fill(color)
    pygame.draw.line(win, (255, 255, 255), (0, 0), (W, H), 10)
    pygame.draw.line(win, (255, 255, 255), (W, 0), (0, H), 10)
    pygame.display.update()

    #TODO 1. Сделать, чтобы окно было чёрным
    #TODO 2. Нарисовать 1 линию
    #TODO 3. Нарисовать 2 линию