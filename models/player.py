import pygame


class Player:
    image_size = 50

    def __init__(self, image_path, screen, nickname, tasks=[], x=0, y=0):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image,
                                            (self.image_size,
                                             self.image_size))
        self.screen = screen
        self.nickname = nickname
        self.tasks = tasks
        self.position = (x, y)

    def display(self):
        self.screen.blit(self.image, self.position)
