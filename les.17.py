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

    win.fill((220, 255, 100))
    win.blit(main_character, (x, y))

    pygame.display.update()
    pygame.time.delay(10)