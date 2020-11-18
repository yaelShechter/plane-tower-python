import pygame
import random
from grid import both_zero

IMAGE = r'plane.png'


class Plane(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Plane, self).__init__()
        self.image = pygame.image.load(IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_plane_randomly(self, scale, grid):
        x = random.randint(-1, 1) * scale
        y = random.randint(-1, 1) * scale
        while both_zero(x, y) or not grid.on_grid(self, x, y):
            x = random.randint(-1, 1) * scale
            y = random.randint(-1, 1) * scale
        self.rect.x += x
        self.rect.y += y

    def move_plane(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_position(self):
        return self.rect.x, self.rect.y
