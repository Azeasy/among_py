import pygame


class Map:
    image_size = 50
    # def __init__(self,
    #              screen,
    #              tasks,
    #              background,
    #              players,
    #              walls,
    #              spawn):  # spawn - это изначальное место, откуда начинается игра

    def __init__(self,
                 map_arr,
                 screen,
                 image_path1,
                 image_path2,
                 background,
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
        '''self.tasks = tasks
        self.players = players
        self.walls = walls
        self.spawn = spawn'''

    def display(self):
        self.screen.blit(self.background)

        for i in range(len(self.map_arr)):
            for j in range(len(self.map_arr[i])):
                if self.map_arr[i][j] == "w":
                    self.screen.blit(self.imageWall, (j * self.image_size, i * self.image_size))
                if self.map_arr[i][j] == "t":
                    self.screen.blit(self.imageTable, (j * self.image_size, i * self.image_size))
