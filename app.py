import pygame
from models.player import Player
from models.map import Map
from models.bot import Bot

skeld = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww3555555555555555555555551wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
    "wwwwww222222222222wwwwwwwwwwwwwwwwwwwwwwwwww235                       51wwwwwwwwwwwwwwwwwwwww2222222222222222wwwwwwwwww",
    "wwwww65555555555554wwwwwwwwwwwwwwwwwwwwwwww355                         51wwwwwwwwwwwwwwwwwww655555555555555554wwwwwwwww",
    "wwwww6            12222222222222222222222235                            512222222222222222223                4wwwwwwwww",
    "wwwww6            5555555555555555555555555           ttttttt            55555555555555555555       tttt b   4wwwwwwwww",
    "wwwww6ttttttt                                         ttttttt         b                              ttt     4wwwwwwwww",
    "wwwww6                                                ttttttt                                                4wwwwwwwww",
    "wwwww6        7888888888889      7888888889                              78888888888888888886      7888888888wwwwwwwwww",
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
    "w6    tttt     7889   12223   488888888www6          ttttttt   b   4wwwww5555553    12wwwwww9        7wwwwwwwwwwwwwwwww",
    "w6    tttt     4ww6   55555   5555555555555    b     ttttttt       4wwww6tttt         4wwwwwww6     7wwwwwwwwwwwwwwwwww",
    "ww89  tttt     4ww6                                    ttttt       4wwww6       b     4ww6          4wwwwwwwwwwwwwwwwww",
    "wwww9          4ww6                            789            b    4wwwww9           7www6          4wwwwwwwwwwwwwwwwww",
    "wwwww8888888888wwww8888888888888888888888888888www89               4wwwwww9         7wwwww8888888888wwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww888888888888888wwwwwwww888888888wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
]
mirahq = [
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww22222222222222222222wwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww222235555555555555555555512222wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww655555                    555554wwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6               b              4wwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6                              4wwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6                              4wwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww8888888888889    7888888888888wwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww22222222222wwwwwwwwwwwwwwwwwwwwwwwwwwwwww2222222222222222ww23    1222222222222222222www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6555555555554wwwwwwwwwwwwwwwwwwwwwwwwwwww6555555555555555513        135555555555555554ww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6           4222222222ww2222222222222wwww6                55        55        b      4ww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6     b     46555555554655555555555556www6       b                                   4ww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6           46        46             6www6                                           4ww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6           13        13             6www6                46        46       b       4ww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6           55    b   55             6www6                46        46               4ww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6                              b    7wwwww8888888888888888w6        4w888888888888888www",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6                                   1wwwwwwwwwwwwwwwwwwwwww6        4wwwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6           79                       6wwwwwwwwwwwwwwwwww7223        12wwwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww88888888888w6      78888888888888888w72222222222229ww723           551wwwwwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww9886   48wwwwwwwwwwwww32225555555555552223               5122wwwwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww644   554wwwww222222w6                           2       55512wwwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6       4wwww655555546                          789         554wwwwwwwwwww",
    "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww6       46ww46      46          7889           73w19          4wwwwwwwwwww",
    "wwwwww22222222222222222222wwwwwwwwwwwwwwwwwww6       46ww46      46     78888wwww8889 7888883www189        12222222222w",
    "wwwww6555555555555555555554wwwwwwwwwwwwwwwwww6       46ww46      13     4w222222222228222222222297223      55555555554w",
    "wwwww6                    4wwwwwwwwwwwwwwwwww6       46ww46      55     13555555555554655555555546555                4w",
    "wwwww6                b   4wwwwwwwwwwwwwwwwww6     12222223             55           46         46                   4w",
    "wwwww6                    4wwwwwwwwwwwwwwwwww6     55555555                   b      46    b    46                   4w",
    "wwwww6                    4wwwwwwwwwwwwwwwwww6                   79                  46         46                   4w",
    "wwwww6             7      4wwwwwwwwwwwwwwwwww6                   46     79           46         46                   4w",
    "wwwww6             122222222222222222222222222222222222222222222223     4w22222222222ww89       12226         789    4w",
    "wwwwww8888889      555555555555555555555555555555555555555555555555     13555555555554ww3       55553         123    4w",
    "wwwwwwwwwwww6                                                           55           4w65           5         555    1w",
    "wwwwwwwwwwww6                             b                                          4w6                             6w",
    "wwwwwwwwwwww6                                                                   b    4w6                             6w",
    "wwwwwwwwwwww6                              788888888888888888888889     79           4w6            98888888888888888ww",
    "wwwwwwwwwwwww888888888888888888888888888888wwwwwwwwwwwwwwwwwwwwwwww88888ww88888888888www888888888888wwwwwwwwwwwwwwwwwww",
]


def start(username="Azeasy", color="Green", level="SKELD"):

    # pygame.init()

    pygame.mixer.init()
    walk_sound = pygame.mixer.Sound('static/audio/walking.ogg')

    size = (1024, 720)
    fps = 30  # Frames per second
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    walking_is_playing = False
    pygame.display.update()

    if level == "SKELD":
        arr = skeld
        x = 3000
        y = 320
    elif level == "MIRA HQ":
        arr = mirahq
        x = 300
        y = 1300

    cam_x, cam_y = -x + 500, -y + 600

    player = None
    player = Player(f"static/images/{color.lower()}.png", screen, username, x=x, y=y, speed=2)

    map_ = None
    map_ = Map(arr,
               screen,
               background="static/images/background.jpg",
               )
    map_.add_player(player)

    animation_step = 0
    done = False
    direction = set()
    gameover = False
    display_hint = True

    map_.display(cam_x, cam_y)

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

            if keys[pygame.K_SPACE]:
                display_hint = False

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

            if pygame.mouse.get_pressed()[0] and \
                    event.type == pygame.MOUSEBUTTONDOWN and \
                    map_.players[0].bullets_cnt > 0:
                map_.players[0].shot(event.pos[0] - cam_x, event.pos[1] - cam_y)

        x, y = map_.players[0].position

        if x + cam_x > size[0] * 0.6:
            cam_x = cam_x - 8
        if x + cam_x < size[0] * 0.4:
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

        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(f'{map_.players[0].bullets_cnt} bullets left', True, white)
        textRect = text.get_rect()
        textRect.center = (size[0] // 2, 50)
        screen.blit(text, textRect)

        text = font.render(f'{alived - 1} imposters left', True, white)
        textRect = text.get_rect()
        textRect.center = (size[0] // 2, 80)
        screen.blit(text, textRect)

        if display_hint:
            red = (255, 0, 0)
            font = pygame.font.Font('static/fonts/mono.otf', 90)
            text = font.render(f'TIME SLOWS DOWN', True, red)
            textRect = text.get_rect()
            textRect.center = (size[0] // 2, size[1] // 2 - 100)
            screen.blit(text, textRect)

            text = font.render(f'WHEN YOU DO NOT MOVE', True, red)
            textRect = text.get_rect()
            textRect.center = (size[0] // 2, size[1] // 2)
            screen.blit(text, textRect)

            text = font.render(f'PRESS SPACE', True, red)
            textRect = text.get_rect()
            textRect.center = (size[0] // 2, size[1] // 2 + 100)
            screen.blit(text, textRect)

        if map_.players[0].lifes <= 0 or alived - 1 == 0:
            gameover = True
            done = True

        pygame.display.flip()
        clock.tick(fps)

    while gameover:
        screen.blit(map_.gameover, (0, 0))

        white = (255, 255, 255)
        font = pygame.font.Font('static/fonts/among_us.ttf', 36)
        text = font.render(f'Press Space to continue', True, white)
        textRect = text.get_rect()
        textRect.center = (size[0] // 2, 50)
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                gameover = False

        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    start()
