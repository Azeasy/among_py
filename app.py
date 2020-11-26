import pygame
from models.player import Player
from models.map import Map
from models.bot import Bot

pygame.init()
size = (1024, 768)
fps = 30  # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cam_x, cam_y = 0, 0

x = 300
y = 300

player = Player("static/images/green.png", screen, "Azeasy", x=x, y=y, speed=2)

arr = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww             x            wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "www            wwwwwwwwwwwwwwwwwwwwwwwwww                            wwwwwwwwwwwwwwwwwwwww                       www",
    "www            wwwwwwwwwwwwwwwwwwwwwwwwd           ttttttt            dwwwwwwwwwwwwwwwwwww                       www",
    "www                                                ttttttt                                                       www",
    "www                                                ttttttt                                                       www",
    "www         wwwwwwwwwwww      wwwwwwwwwd                              dwwwwwwwwwwwwwwwwwwwwwwww       wwwwwwwwwwwwww",
    "wwwwww      wwwwwwwwwwww      wwwwwwwwwww              b              wwwwwwwwwwwwwwwwwwwwwwwww       wwwwwwwwwwwwww",
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

animation_step = 0
done = False
direction = set()

bullets_cnt = 10

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

        if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
            bullets_cnt -= 1
            map_.players[0].shot(event.pos[0] - cam_x, event.pos[1] - cam_y)

    x, y = map_.players[0].position

    if x + cam_x > size[0]*0.7:
        cam_x = cam_x - 7
    if x + cam_x < size[0]*0.3:
        cam_x = cam_x + 9

    if y + cam_y > size[1]*0.6:
        cam_y = cam_y - 7
    if y + cam_y < size[1]*0.3:
        cam_y = cam_y + 9


    # Draw
    # map_.display(cam_x, cam_y)
    screen.blit(map_.background, (0, 0))

    freq = fps // 3
    animation_step += 1
    animation_step %= freq

    bullet_speed = 0.3
    if len(direction) > 0:
        bullet_speed = 1

    for player in map_.players:
        if player.lifes <= 0:
            continue
        player.move(direction=direction, map_arr=arr, cam_x=cam_x, cam_y=cam_y)
        player.display(cam_x,
                       cam_y,
                       direction=direction,
                       bullet_speed=bullet_speed,
                       step=animation_step,
                       frequency=freq // 2,
                       players=map_.players)
        if isinstance(player, Bot):
            player.shot(x, y)

    map_.display(cam_x, cam_y)

    if map_.players[0].lifes <= 0:
        game_over = True

    pygame.display.flip()
    clock.tick(fps)
