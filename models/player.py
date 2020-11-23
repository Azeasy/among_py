import pygame


class Player:
    image_size = 100

    def __init__(self, image_path, screen, nickname, tasks=[], x=0, y=0, speed=1):
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
        self.tasks = tasks
        self.position = (x, y)
        self.speed = speed
        self.animate = False
        self.cur_dir = 'right'

    def display(self, direction, step=0, frequency=10):
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

        self.screen.blit(self.image, self.position)

    def move(self, direction):
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

        self.position = (cur_x, cur_y)

    def __str__(self):
        return f"{self.__class__.__name__} {self.nickname}"

    def __repr__(self):
        return self.__str__()
