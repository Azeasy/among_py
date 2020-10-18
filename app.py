import pygame
from models.player import Player

pygame.init()
size = (1024, 768)
fps = 20  # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = 100
y = 100

player = Player("test_block.png", screen, "Azeasy", x=x, y=y)
player2 = Player("test_block.png", screen, "Azeasy", x=x + 30, y=y - 10)

i = 0
# Game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw
    screen.fill((100, 100, 255))

    player.position = (x + i, y + i)
    player.display()

    player2.position = (x + i + 30, y + i - 10)
    player2.display()

    i += 1

    pygame.display.flip()
    clock.tick(fps)
