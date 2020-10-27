import pygame


class Map:
    def __init__(self,
                 screen,
                 tasks,
                 background,
                 players,
                 walls,
                 spawn):  # spawn - это изначальное место, откуда начинается игра

        self.screen = screen
        self.background = pygame.image.load(background)
        self.tasks = tasks
        self.players = players
        self.walls = walls
        self.spawn = spawn

    def display(self):
        self.screen.blit(self.background, (0, 0))
