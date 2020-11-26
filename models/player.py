import pygame
import time
from .bullet import Bullet
from .utils import is_collide


class Player:
    image_size = 100

    def __init__(self, image_path, screen, nickname, cooldown=3, x=0, y=0, speed=1, lifes=3):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image,
                                            (self.image_size,
                                             self.image_size))

        image_left = pygame.image.load(image_path.replace('.png', '_left.png'))
        self.image_left = pygame.transform.scale(image_left,
                                                 (self.image_size,
                                                  self.image_size))
        image_right = pygame.image.load(image_path.replace('.png', '_right.png'))
        self.image_right = pygame.transform.scale(image_right,
                                                  (self.image_size,
                                                   self.image_size))
        image_right_jump = pygame.image.load(image_path.replace('.png', '_right_jump.png'))
        self.image_right_jump = pygame.transform.scale(image_right_jump,
                                                       (self.image_size,
                                                        self.image_size))
        image_left_jump = pygame.image.load(image_path.replace('.png', '_left_jump.png'))
        self.image_left_jump = pygame.transform.scale(image_left_jump,
                                                      (self.image_size,
                                                       self.image_size))
        self.screen = screen
        self.nickname = nickname
        self.position = (x, y)
        self.speed = speed
        self.animate = False
        self.cur_dir = 'right'
        self.bullets = []
        self.cooldown = cooldown
        self.last_shot = 0
        self.lifes = lifes

    def display(self, cam_x, cam_y, direction, bullet_speed=1, step=0, frequency=10, players=[]):
        animate = len(direction) > 0
        if 'left' in direction:
            self.image = self.image_left
            self.cur_dir = 'left'
        elif 'right' in direction:
            self.image = self.image_right
            self.cur_dir = 'right'

        if animate:
            if self.cur_dir == 'left':
                if step < frequency:
                    self.image = self.image_left_jump
                else:
                    self.image = self.image_left
            elif self.cur_dir == 'right':
                if step < frequency:
                    self.image = self.image_right_jump
                else:
                    self.image = self.image_right
        else:
            if self.cur_dir == 'left':
                self.image = self.image_left
            elif self.cur_dir == 'right':
                self.image = self.image_right

        self.screen.blit(self.image, (self.position[0] + cam_x, self.position[1] + cam_y))

        for bullet in self.bullets:
            bullet.move(speed=bullet_speed, players=players)
            bullet.display(cam_x, cam_y)

    def move(self, direction, map_arr, cam_x, cam_y):
        cur_pos = self.position
        cur_x, cur_y = cur_pos[0], cur_pos[1]

        reduce_speed = 1
        if len(direction) > 1:
            reduce_speed = 2 ** 0.5

        if 'up' in direction:
            cur_y -= 5 * self.speed / reduce_speed
        if 'down' in direction:
            cur_y += 5 * self.speed / reduce_speed
        if 'left' in direction:
            cur_x -= 5 * self.speed / reduce_speed
        if 'right' in direction:
            cur_x += 5 * self.speed / reduce_speed

        collide = is_collide((cur_x, cur_y), map_arr)

        if not collide:
            self.position = (cur_x, cur_y)

    def shot(self, dest_x, dest_y):
        start = self.last_shot
        x, y = self.position
        if time.time() - start > self.cooldown:
            self.bullets.append(Bullet(self.screen, x + 25, y + 25, dest_x, dest_y))
            self.last_shot = time.time()

    def __str__(self):
        return f"{self.__class__.__name__} {self.nickname}"

    def __repr__(self):
        return self.__str__()
