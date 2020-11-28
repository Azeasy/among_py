import pygame


def is_collide(pos, map_arr, block_size=50, self_size=50):
    x, y = pos

    rect1 = pygame.Rect(x, y, self_size, self_size)
    collide = False
    for i in range(len(map_arr)):
        for j in range(len(map_arr[i])):
            if map_arr[i][j] in 'wd123456789':
                rect2 = pygame.Rect(j * block_size,
                                    i * block_size,
                                    block_size,
                                    block_size)
                if rect1.colliderect(rect2):
                    collide = True
    return collide
