import random
import pygame as pg
W, H = (1000, 500)
class inginirium(pg.sprite.Sprite):
    def __init__(self, * group):
        super().__init__(*group)
        self.image = pg.image.load("Gyro/pizza.jpg")
        self.image = pg.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) -1,
                                   random.randrange(3) - 1)


a_s = pg.sprite.Group()
for i in range(50):
    inginirium(a_s)

win = pg.display.set_mode((1000, 500))
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    a_s.update()

    win.fill((255, 255, 255))
    a_s.draw(win)
    pg.display.update()

