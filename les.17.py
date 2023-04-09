import pygame.draw
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 200
y = 200
v = 3
main_character = pygame.image.load("image/Kakyoin.png")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= v
    elif keys[pygame.K_RIGHT]:
        x += v
    elif keys[pygame.K_UP]:
        y -= v
    elif keys[pygame.K_DOWN]:
        y += v
    else:
        if x > 200:
             x -= 1
        elif x < 200:
            x += 1
        if y > 200:
            y -= 1
        elif y < 200:
            y += 1


    if y < 100 or y > 400 or x < 100 or x > 400:
        color = (255, 0, 0)
        v  = 1
        rad = 50
    else:
        color = (0, 255, 0)
        v = 5
        rad = 50

    win.fill((220, 255, 100))

    pygame.draw.circle(win, color, (x + 50, y + 50), 50)
    win.blit(main_character, (x, y))

    pygame.display.update()
    pygame.time.delay(10)