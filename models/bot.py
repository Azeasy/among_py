from .player import Player
from .bullet import Bullet
from random import choices
import time


class Bot(Player):
    slow_mo = True
    directions = ['left', 'right', 'up', 'down']

    def __init__(self, image_path, screen, nickname, x=300, y=300, speed=1, cooldown=3, lifes=3, **kwargs):
        super().__init__(image_path, screen, nickname, cooldown=cooldown, x=x, y=y, speed=speed, lifes=lifes)
        self.direction = choices(self.directions, k=2)
        self.duration = 2
        self.last_move = None

    def display(self, cam_x, cam_y, direction, bullet_speed=1, step=0, frequency=10, players=[], map_arr=[]):
        super(Bot, self).display(cam_x, cam_y, self.direction, bullet_speed, step, frequency, players, map_arr)

    def move(self, direction, map_arr, cam_x, cam_y):
        if 'right' in self.direction and 'left' in self.direction or \
                'up' in self.direction and 'down' in self.direction:
            self.direction = []

        self.slow_mo = len(direction) > 0

        if self.slow_mo:
            self.speed = 1
        else:
            self.speed = 0.3

        super(Bot, self).move(self.direction, map_arr, cam_x, cam_y)

        start = time.time() // 1

        if start % self.duration == 0 and self.last_move != start % 10:
            self.direction = choices(self.directions, k=2)
            self.last_move = start % 10

    def shot(self, dest_x, dest_y):
        x, y = self.position

        distance = ((dest_x - x) ** 2 + (dest_y - y) ** 2) ** 0.5

        if distance < 500:
            super(Bot, self).shot(dest_x, dest_y)
