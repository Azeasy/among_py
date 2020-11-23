import pygame
from models.player import Player
from models.map import Map

pygame.init()
size = (1024, 768)
fps = 30  # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = 100
y = 100

player = Player("static/images/green.png", screen, "Azeasy", x=x, y=y, speed=2)
player2 = Player("static/images/green.png", screen, "Azeasy1", x=x, y=y, speed=1)

arr = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww             x            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "www            wwwwwwwwwwwwwwwwwwwwwwwwww                            wwwwwwwwwwwwwwwwwwwww                       www",
    "www         b  wwwwwwwwwwwwwwwwwwwwwwwwd           ttttttt            dwwwwwwwwwwwwwwwwwww                       www",
    "www                                                ttttttt                                                       www",
    "www        b                                       ttttttt                                                       www",
    "www         wwwwwwwwwwww      wwwwwwwwwd                              dwwwwwwwwwwwwwwwwwwwwwwww       wwwwwwwwwwwwww",
    "wwwwww      wwwwwwwwwwww      wwwwwwwwwww                             wwwwwwwwwwwwwwwwwwwwwwwww       wwwwwwwwwwwwww",
    "wwwwww      wwwwwwwwwwww      wwwwwwwwwwwww                         wwwwwwwwwww                                   ww",
    "    ww      ww      ww        wwwwwwwwwwwwwwwwwwwwd        dwwwwwwwwww                                            ww",
    "     w      w       ww              wwwwwwwwwwwwwww          wwwwwwwww                                            ww",
    "                    ww               wwwwwwwwwwwwww          wwwwwwwww                                            ww",
]

map_ = Map(arr,
           screen,
           "static/images/test_block.png",
           "static/images/green.png",
           "static/images/background.jpg",
           # [player, player2]
           )
map_.add_player(player)
map_.add_player(player2)

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

        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())

    # Draw
    map_.display()

    freq = fps // 3
    animation_step += 1
    animation_step %= freq

    for player in map_.players:
        player.move(direction=direction)
        player.display(direction=direction, step=animation_step, frequency=freq // 2)

    pygame.display.flip()
    clock.tick(fps)
