import pygame
from .bot import Bot


class Map:
    image_size = 50

    # def __init__(self,
    #              tasks,
    #              spawn):  # spawn - это изначальное место, откуда начинается игра

    def __init__(self,
                 map_arr,
                 screen,
                 background,
                 players=[],
                 data_path='static/images/{}.png'
                 ):

        self.screen = screen
        self.background = pygame.image.load(background)
        self.map_arr = map_arr
        self.players = players
        self.data_path = data_path
        self.assets = {}

    def add_player(self, player):
        add = False
        for pl in self.players:
            if pl.nickname == player.nickname:
                return
        self.players.append(player)

    def get_asset(self, s):
        if not self.assets.get(s):
            image = pygame.image.load(self.data_path.format(s))
            self.assets[s] = pygame.transform.scale(image,
                                                    (self.image_size,
                                                     self.image_size))
        return self.assets.get(s)

    def display_ground(self, cam_x, cam_y):
        for i in range(len(self.map_arr)):
            for j in range(len(self.map_arr[i])):
                if self.map_arr[i][j] == " ":
                    self.screen.blit(self.get_asset('ground'),
                                     (j * self.image_size + cam_x, i * self.image_size + cam_y))

    def display(self, cam_x, cam_y):
        for i in range(len(self.map_arr)):
            for j in range(len(self.map_arr[i])):
                if self.map_arr[i][j] not in " b":
                    self.screen.blit(self.get_asset(self.map_arr[i][j]),
                                     (j * self.image_size + cam_x, i * self.image_size + cam_y))
                if self.map_arr[i][j] == "b":
                    self.add_player(Bot("static/images/red.png",
                                        self.screen,
                                        str(len(self.players)),
                                        x=j * self.image_size,
                                        y=i * self.image_size,
                                        speed=2,
                                        lifes=1))
                    self.map_arr[i] = self.map_arr[i][:j] + ' ' + self.map_arr[i][j + 1:]
