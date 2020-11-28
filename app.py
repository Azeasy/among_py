import pygame
from models.player import Player
from models.map import Map
from models.bot import Bot

pygame.mixer.init()
kill_sound = pygame.mixer.Sound('static/audio/kill.ogg')
walk_sound = pygame.mixer.Sound('static/audio/walking.ogg')

skeld = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww3555555555555555555555551wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwww222222222222wwwwwwwwwwwwwwwwwwwwwwwwww235                       51wwwwwwwwwwwwwwwwwwwww2222222222222222wwwwwwwwww",
    "wwwww65555555555554wwwwwwwwwwwwwwwwwwwwwwww35                          51wwwwwwwwwwwwwwwwwww655555555555555554wwwwwwwww",
    "wwwww6            12222222222222222222222235                            512222222222222222223                4wwwwwwwww",
    "wwwww6            5555555555555555555555555           ttttttt            55555555555555555555       tttt b   4wwwwwwwww",
    "wwwww6ttttttt                                         ttttttt                                        ttt     4wwwwwwwww",
    "wwwww6                                                ttttttt                                                4wwwwwwwww",
    "wwwww6        7888888888889      7888888889                              d8888888888888888886      7888888888wwwwwwwwww",
    "w2222w889     4ww222222ww23      122wwwwwww9                             4ww22355555555122226      1222wwwww2222222wwww",
    "6555522w6     4w65555554655      5554wwwwwww89                         78w23555        555555      555512223       1www",
    "6    5522     123  tt  46           4wwwwwwwww88888889          7888888ww655                           55555        1ww",
    "6      55     555      46           12222wwwwwwwwwwww6          4wwwwwwww6                                          t1w",
    "6ttt                   46           555554wwwwwwwwwww6          122222222w9            7888889                      tt4",
    "6ttt                b  46                1wwwwwwwwwww6          5555555554w222222222222wwwwww6         78889        t7w",
    "6      79     789      46                 4wwwwwwwwww6                   55555555555555555www6         4www6        7ww",
    "6    7ww6     4w6      46              b  4wwwwwwwwww6                                    4ww6     7888wwww6       7www",
    "w8888www6     4ww888888w6                7wwwwwwwwwww6          78889      ttttttttt      4ww6     4wwwwwwww8888888wwww",
    "wwwwwwww6     1222wwwwwww88555555555555554wwwww2222223          12223                     4ww6     4wwwwwwwwwwwwwwwwwww",
    "wwwwwwww6     55551222wwww6              4www235555555          55555                     5555     1wwwwwwwwwwwwwwwwwww",
    "ww22222226        55554www6tttttttt      4w2355           b                                         1wwwwwwwwwwwwwwwwww",
    "ww5555556             4www6tttttttt      4655                                                        1wwwwwwwwwwwwwwwww",
    "w6                    4www6            78w6                        7888888888889    78888889          4wwwwwwwwwwwwwwww",
    "w6tttttttt     7889   12223   488888888www6          ttttttt   b   4wwwww5555553    12wwwwww9        7wwwwwwwwwwwwwwwww",
    "w6tttttttt     4ww6   55555   5555555555555    b     ttttttt       4wwww6tttt         4wwwwwww6     7wwwwwwwwwwwwwwwwww",
    "ww89tttttt     4ww6                                    ttttt       4wwww6       b     4ww6          4wwwwwwwwwwwwwwwwww",
    "wwww9          4ww6                            789            b    4wwwww9           7www6          4wwwwwwwwwwwwwwwwww",
    "wwwww8888888888wwww8888888888888888888888888888www89               4wwwwww9         7wwwww8888888888wwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww888888888888888wwwwwwww888888888wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
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
    "wwwwww                    wwwwwwwwwwwwwwwwwwww       ww  ww             ww           ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwwwww   wwwwwwww                          ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww                   ww     ww           ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww                   ww     ww           ww         ww                   ww",
    "wwwwww                    wwwwwwwwwwwwwwwwwwww                   ww     wwwwwwwwwwwwwwwww       wwwww                ww",
    "wwwwwwwwwwwww      wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww     ww           wwww           w                ww",
    "wwwwwwwwwwwww                                                                        wwwwwwww       w          wwwwwwww",
    "wwwwwwwwwwwww                                                                        www                             ww",
    "wwwwwwwwwwwww                                                           ww      b    www                             ww",
    "wwwwwwwwwwwww                              wwwwwwwwwwwwwwwwwwwwwwww     ww           www            wwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
]


def start(username="Azeasy", color="Green", level="SKELD"):
    pygame.init()
    size = (1024, 768)
    fps = 30  # Frames per second
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    walking_is_playing = False

    if level == "SKELD":
        arr = skeld
        x = 3000
        y = 320
    elif level == "MIRA HQ":
        arr = mirahq
        x = 300
        y = 1300

    cam_x, cam_y = -x + 500, -y + 600

    player = Player(f"static/images/{color.lower()}.png", screen, "Azeasy", x=x, y=y, speed=2)

    map_ = Map(arr,
               screen,
               background="static/images/background.jpg",
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
                if event.key == pygame.K_UP:
                    if 'up' in direction:
                        direction.remove('up')
                if event.key == pygame.K_DOWN:
                    if 'down' in direction:
                        direction.remove('down')
                if event.key == pygame.K_RIGHT:
                    if 'right' in direction:
                        direction.remove('right')
                if event.key == pygame.K_LEFT:
                    if 'left' in direction:
                        direction.remove('left')

            if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
                bullets_cnt -= 1
                map_.players[0].shot(event.pos[0] - cam_x, event.pos[1] - cam_y)

        x, y = map_.players[0].position

        if x + cam_x > size[0] * 0.7:
            cam_x = cam_x - 8
        if x + cam_x < size[0] * 0.3:
            cam_x = cam_x + 8

        if y + cam_y > size[1] * 0.6:
            cam_y = cam_y - 7
        if y + cam_y < size[1] * 0.3:
            cam_y = cam_y + 7

        # Draw
        # map_.display(cam_x, cam_y)
        screen.blit(map_.background, (0, 0))

        freq = fps // 3
        animation_step += 1
        animation_step %= freq

        bullet_speed = 0.1
        if len(direction) > 0:
            bullet_speed = 1
            if not walking_is_playing:
                walk_sound.play()
                walking_is_playing = True
        else:
            walk_sound.stop()
            walking_is_playing = False

        alived = len(map_.players)

        map_.display_ground(cam_x, cam_y)

        for player in map_.players:
            if not player.is_alive():
                player.dead(cam_x, cam_y, bullet_speed=bullet_speed, players=map_.players)
                alived -= 1
                continue
            player.move(direction=direction, map_arr=arr, cam_x=cam_x, cam_y=cam_y)
            player.display(cam_x,
                           cam_y,
                           direction=direction,
                           bullet_speed=bullet_speed,
                           step=animation_step,
                           frequency=freq // 2,
                           players=map_.players,
                           map_arr=map_.map_arr)
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

        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'{bullets_cnt} bullets left', True, green)
        textRect = text.get_rect()
        textRect.center = (130, 50)
        screen.blit(text, textRect)

        text = font.render(f'{alived - 1} imposters left', True, green)
        textRect = text.get_rect()
        textRect.center = (130, 100)
        screen.blit(text, textRect)
        if map_.players[0].lifes <= 0:
            done = True

        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    start()
