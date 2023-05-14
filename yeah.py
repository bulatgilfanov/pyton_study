import pygame
import random

FPS = 60
W, H = 500, 500

clock = pygame.time.Clock()
pygame.init()

win = pygame.display.set_mode((W, H))
win.fill((255, 255, 255))

size = 200
flag =5
object_to_draw = "circle"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    color = random.choices(range(256), k=3)
    pos = pygame.mouse.get_pos()

    if object_to_draw == "circle":
        pygame.draw.circle(win, (color), pos, size)
    elif object_to_draw == "rect":
        pygame.draw.rect(win, (color), (pos[0] - size // 2, pos[1] - size // 2, size, size))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        object_to_draw = "rect"
    elif keys[pygame.K_q]:
        object_to_draw = "circle"
    elif keys[pygame.K_SPACE]:
        win.fill((255, 255, 255))


    size += flag
    if size > 200:
        flag = flag * (-1)
    if size < 50:
        flag = flag * (-1)

    pygame.display.update()