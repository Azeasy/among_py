import pygame
from math import cos, sin, atan, pi, degrees
from .utils import is_collide


class Bullet:
    image_size = 30

    def __init__(self,
                 screen,
                 x,
                 y,
                 dest_x,
                 dest_y,
                 ):
        image = pygame.image.load('static/images/bullet.png')
        self.image = pygame.transform.scale(image,
                                            (self.image_size,
                                             self.image_size))
        self.screen = screen
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.x_diff = dest_x - x
        self.y_diff = dest_y - y

    def display(self, cam_x, cam_y):
        self.screen.blit(self.image, (self.x + cam_x, self.y + cam_y))

    def move(self, speed=1, players=[], map_arr=[]):
        if self.x_diff == 0:
            angle = atan(self.y_diff * 10 ** 6)
        else:
            angle = atan(self.y_diff / self.x_diff)

        if self.x_diff >= 0 and self.y_diff >= 0:
            part = 1
        elif self.x_diff <= 0 and self.y_diff >= 0:
            part = 2
        elif self.x_diff <= 0 and self.y_diff <= 0:
            part = 3
        elif self.x_diff >= 0 and self.y_diff <= 0:
            part = 4

        value = 15

        if part == 1:
            self.x += value * cos(angle) * speed
            self.y += value * sin(angle) * speed
        elif part == 2:
            self.x -= value * cos(angle) * speed
            self.y -= value * sin(angle) * speed
        elif part == 3:
            self.x -= value * cos(angle) * speed
            self.y -= value * sin(angle) * speed
        elif part == 4:
            self.x += value * cos(angle) * speed
            self.y += value * sin(angle) * speed

        for player in players:
            distance = ((player.position[0] + 25 - self.x) ** 2 +
                        (player.position[1] + 25 - self.y) ** 2) ** 0.5

            if distance < 50 and self not in player.bullets and player.lifes > 0:
                player.get_punch()
                self.destroy(players)
                break

        if is_collide((self.x, self.y), map_arr=map_arr, self_size=self.image_size):
            self.destroy(players)

    def destroy(self, players):
        for player in players:
            if self in player.bullets:
                player.bullets.remove(self)
                break
