import pygame as pg
import random

MAROON = [128, 0, 0]
BLACK = [0] * 3
RED = [255, 0, 0]
W, H = 500, 500

pg.init()
win = pg. display.set_mode((W, H))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for i in range(10):
        pg.draw.circle(win, MAROON,
                       (random.randint(0, W), random.randint(0, H)), 1)

    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, RED, pos, 5)
    pg.display.update()

    pg.time.delay(20)