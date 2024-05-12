import pygame
import time

from setting import *


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, path, pos, name):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.path = path
        self.rect = pos
        self.name = name
        self.image = self.get_image()


    def get_image(self):
        image = pygame.image.load(self.path).convert_alpha()
        image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))
        return image


    def update(self):
        pass
    

    