import pygame
from models.player import Player

pygame.init()
size = (1024, 768)
fps = 30  # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = 100
y = 100

player = Player("static/images/green.png", screen, "Azeasy", x=x, y=y, speed=2)

animation_step = 0
done = False
direction = set()

# Game loop
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            direction.add('up')
        if keys[pygame.K_DOWN]:
            direction.add('down')
        if keys[pygame.K_RIGHT]:
            direction.add('right')
        if keys[pygame.K_LEFT]:
            direction.add('left')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:  # What exactly did we press?
                direction.remove('up')
            if event.key == pygame.K_DOWN:
                direction.remove('down')
            if event.key == pygame.K_RIGHT:
                direction.remove('right')
            if event.key == pygame.K_LEFT:
                direction.remove('left')

    player.move(direction=direction)

    # Draw
    screen.fill((100, 100, 255))

    freq = fps // 3
    animation_step += 1
    animation_step %= freq
    player.display(direction=direction, step=animation_step, frequency=freq//2)

    pygame.display.flip()
    clock.tick(fps)
