import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col

    def draw(self, win):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1
        if keys[pygame.K_RIGHT]:
            self.x += 1


circle0 = Circle(250, 250, 70, (255, 0, 0))
circle1 = Circle(250, 150, 50, (255, 0, 0))
circle2 = Circle(190, 190, 30, (255, 255, 255))
circle3 = Circle(300, 190, 30, (255, 255, 255))

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit()


    win.fill((255, 55, 46))
    circle0.draw(win)
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)

    circle0.move_by_keys()
    circle1.move_by_keys()
    circle2.move_by_keys()
    circle3.move_by_keys()
    pygame.display.update()
