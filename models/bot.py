from .player import Player
from random import choices, randint
import time


class Bot(Player):
    slow_mo = True
    directions = ['left', 'right', 'up', 'down']

    def __init__(self, image_path, screen, nickname, x=300, y=300, speed=1, cooldown=3, **kwargs):
        super().__init__(image_path, screen, nickname, x=x, y=y, speed=1)
        self.direction = choices(self.directions, k=2)
        self.duration = 2
        self.last_move = None
        self.bullets = []
        self.cooldown = cooldown
        self.last_shot = None

    def display(self, direction, step=0, frequency=10):
        super(Bot, self).display(direction, step, frequency)

        for bullet in self.bullets:
            bullet.move()
            bullet.display()

    def move(self, direction):
        self.slow_mo = len(direction) > 0

        if self.slow_mo:
            self.speed = 1
        else:
            self.speed = 0.5

        super(Bot, self).move(self.direction)

        start = time.time() // 1

        if start % self.duration == 0 and self.last_move != start % 10:
            self.direction = choices(self.directions, k=2)
            self.last_move = start % 10

    def shot(self, players):
        for player in players:
            if isinstance(player, Player):
                x, y = self.position
                dest_x, dest_y = player.position

                distance = ((dest_x - x)**2 + (dest_y - y)**2)**0.5

                if distance < 500:
                    start = time.time() // 1
                    if start % self.cooldown == 0 and self.last_shot != start % 10:
                        # self.bullets.append(Bullet(self.screen, x, y, dest_x, dest_y))
                        self.last_shot = start % 10
                        pass
