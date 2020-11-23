import pygame
from .player import Player
from .bot import Bot


class Map:
    image_size = 50

    # def __init__(self,
    #              tasks,
    #              spawn):  # spawn - это изначальное место, откуда начинается игра

    def __init__(self,
                 map_arr,
                 screen,
                 image_path1,
                 image_path2,
                 background,
                 players=[],
                 ):

        imageWall = pygame.image.load(image_path1)
        self.imageWall = pygame.transform.scale(imageWall,
                                                (self.image_size,
                                                 self.image_size))
        imageTable = pygame.image.load(image_path2)
        self.imageTable = pygame.transform.scale(imageTable,
                                                 (self.image_size,
                                                  self.image_size))

        self.screen = screen
        self.background = pygame.image.load(background)
        self.map_arr = map_arr
        self.players = players
        # self.tasks = tasks
        # self.walls = walls
        # self.spawn = spawn

    def add_player(self, player):
        add = False
        for pl in self.players:
            if pl.nickname == player.nickname:
                return
        self.players.append(player)

    def display(self):
        self.screen.blit(self.background, (0, 0))

        for i in range(len(self.map_arr)):
            for j in range(len(self.map_arr[i])):
                if self.map_arr[i][j] == "w":
                    self.screen.blit(self.imageWall, (j * self.image_size, i * self.image_size))
                if self.map_arr[i][j] == "t":
                    self.screen.blit(self.imageTable, (j * self.image_size, i * self.image_size))
                if self.map_arr[i][j] == "b":
                    self.add_player(Bot("static/images/green.png",
                                        self.screen,
                                        "Azeasy3",
                                        x=j * self.image_size,
                                        y=i * self.image_size,
                                        speed=1))
