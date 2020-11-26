import pygame
from models.player import Player
from models.map import Map
from models.bot import Bot
import time

skeld = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                       wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                          wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwww            wwwwwwwwwwwwwwwwwwwwwwwwww                            wwwwwwwwwwwwwwwwwwwww                wwwwwwwwww",
    "wwwwwwttttttt     wwwwwwwwwwwwwwwwwwwwwwwww           ttttttt            dwwwwwwwwwwwwwwwwwww       tttt b   wwwwwwwwww",
    "wwwwwwttttttt                                         ttttttt                                        ttt     wwwwwwwwww",
    "wwwwww                                                ttttttt                                                wwwwwwwwww",
    "wwwwww        wwwwwwwwwwwww      wwwwwwwwww                              dwwwwwwwwwwwwwwwwwww      wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwww     wwwwwwwwwwwww      wwwwwwwwwww                             wwwwwwwwwwwwwwwwwwww      wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwww     wwwwwwwwwwwww      wwwwwwwwwwwww                         wwwwwwww        wwwwww      wwwwwwwww       wwww",
    "w    wwww     www  tt  ww           wwwwwwwwwwwwwwwwwd          wwwwwwwwwwww                           wwwww        www",
    "w      ww     www      ww           wwwwwwwwwwwwwwwwww          wwwwwwwww                                           tww",
    "wttt                   ww           wwwwwwwwwwwwwwwwww          wwwwwwwww              wwwwwwwwwwww                 ttw",
    "wttt                b  ww                wwwwwwwwwwwww          wwwwwwwwwwwwwwwwwwwwwwwwwwwwww         wwwww        tww",
    "w      ww     www      ww                 wwwwwwwwwwww                   wwwwwwwwwwwwwwwwwwwww         wwwww        www",
    "w    wwww     www      ww              b  wwwwwwwwwwww                                    wwww     wwwwwwwww       wwww",
    "wwwwwwwww     wwwwwwwwwww               wwwwwwwwwwwwww          wwwww      ttttttttt      wwww     wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwww     wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww          wwwww                     wwww     wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwww     wwwwwwwwwwwww              wwwwwwwwwwwww          wwwwwwwwwwwwwwwwwwwwwwwwwwwwww     wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwww        wwwwwwwwwwtttttttt      wwwwww           b                                         wwwwwwwwwwwwwwwwwww",
    "wwwwwwwww             wwwwwtttttttt      wwww                                                        wwwwwwwwwwwwwwwwww",
    "ww                    wwwww            wwww                        wwwwwwwwwwwww    wwwwwwww          wwwwwwwwwwwwwwwww",
    "wwtttttttt     wwww   wwwww   wwwwwwwwwwwww          ttttttt   b   wwwwwwwwwwwww    wwwwwwwww        wwwwwwwwwwwwwwwwww",
    "wwtttttttt     wwww   wwwww   wwwwwwwwwwwww    b     ttttttt       wwwwwwtttt         wwwwwwwww     wwwwwwwwwwwwwwwwwww",
    "wwwwtttttt     wwww                                    ttttt       wwwwww       b     wwww          wwwwwwwwwwwwwwwwwww",
    "wwwww          wwww                            www            b    wwwwwww           wwwww          wwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               wwwwwwww         wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
]
mirahq = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                    wwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                              wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               b              wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                              wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                              wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                              wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww    wwwwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           wwwwwwwwwwwwwwwwwwwwwwwwwwwwww                ww        ww               www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           wwwwwwwwwwwwwwwwwwwwwwwwwwwwww                ww        ww        b      www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           ww        wwwwwwwwwwwwwwwwwwww       b                                   www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           ww        ww             wwwww                                           www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           ww        ww             wwwww                ww        ww               www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           ww    b   ww             wwwww                ww        ww               www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                                    wwwwwwwwwwwwwwwwwwwwwww        wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                                    wwwwwwwwwwwwwwwwwwwwwww        wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           ww                       wwwwwwwwwwwwwwwwwwwwwww        wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww        wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww           wwwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   wwww             wwwwwwwwwwwwwwwwww               wwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww       ww  wwwwwwwwww                           w       wwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww       ww  wwwwwwwwww                          www         wwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww       ww  ww      ww          wwww           wwwww          wwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww       ww  ww      ww          wwww        wwwwwwwwww        wwwwwwwwwwww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww       ww  ww      ww     wwwwwwwwwwwwwwwwwwwwwwwwwwwww      wwwwwwwwwwww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww       ww  ww      ww     ww           ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww       ww  ww             ww           ww         ww         x         ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwwwww   wwwwwwww                          ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww                   ww     ww           ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww                   ww     ww           ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww                   ww     wwwwwwwwwwwwwwwww       wwwww                ww",
    "wwwwwwwwwwwww      wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww     ww           wwww                            ww",
    "wwwwwwwwwwwww                                                                        wwwwwwww       wwwwwww    wwwwwwww",
    "wwwwwwwwwwwww                                                                        www                             ww",
    "wwwwwwwwwwwww                                                           ww      b    www                             ww",
    "wwwwwwwwwwwww                              wwwwwwwwwwwwwwwwwwwwwwww     ww           www            wwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
]


def start(color="Green", level="SKELD"):
    pygame.init()
    size = (1024, 768)
    fps = 30  # Frames per second
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    if level == "SKELD":
        arr = skeld
        x = 3000
        y = 320
    elif level == "MIRA HQ":
        arr = mirahq
        x = 300
        y = 1300

    cam_x, cam_y = 0, 0

    player = Player(f"static/images/{color.lower()}.png", screen, "Azeasy", x=x, y=y, speed=2)

    map_ = Map(arr,
               screen,
               "static/images/wall.png",
               "static/images/table.png",
               "static/images/background.jpg",
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

        if x + cam_x > size[0] * 0.7:
            cam_x = cam_x - 10
        if x + cam_x < size[0] * 0.3:
            cam_x = cam_x + 10

        if y + cam_y > size[1] * 0.6:
            cam_y = cam_y - 12
        if y + cam_y < size[1] * 0.3:
            cam_y = cam_y + 12

        # Draw
        # map_.display(cam_x, cam_y)
        screen.blit(map_.background, (0, 0))

        freq = fps // 3
        animation_step += 1
        animation_step %= freq

        bullet_speed = 0.3
        if len(direction) > 0:
            bullet_speed = 1

        alived = len(map_.players)
        for player in map_.players:
            if player.lifes <= 0:
                alived -= 1
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
            if alived == 1:
                done = True

        map_.display(cam_x, cam_y)

        life_x, life_y = 0, 0
        for i in range(map_.players[0].lifes):
            life = pygame.image.load('static/images/lives.png')
            life = pygame.transform.scale(life,
                                          (30, 30))
            screen.blit(life, (life_x, life_y))
            life_x += 40

        if map_.players[0].lifes <= 0:
            done = True

        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    start()
