import random
import pygame

FPS = 30
pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))

x = 250
y = 250
color = (235, 52, 94)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)

    win.fill((126, 223, 247))
    pygame.draw.rect(win, (150, 100, 62), (0, 400, 500, 100))
    pygame.draw.circle(win, (color), (x, y), 20)

    if y < 380:
        y = y + 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
        color = random.choices(range(256), k=3)
    elif keys[pygame.K_RIGHT]:
        x += 5
        color = random.choices(range(256), k=3)
    elif keys[pygame.K_SPACE]:
        y -= 50