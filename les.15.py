import pygame
pygame.init()
pygame.display.set_mode((600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (2, 235, 155)
    win.fill(color)
    pygame.draw.rect(win, (255, 255, 0), (0, 0, 50, 50))
    pygame.draw.rect(win, (255, 255, 0), (50, 50, 250, 250))
    pygame.draw.circle(win, (255, 0, 0), (250, 250), 100)
    pygame.draw.polygon(win, (0, 0, 0), [(0, 100), (100, 50), (150, 150)], False)
    pygame.draw.line(win, (0, 255, 255), (0, 0), (100, 100), 5)
    pygame.draw.lines(win, (0, 0, 0), True, ((200, 200), (300, 150), (300, 250)), 10)

    pygame.display.update()