import pygame
import time


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, name, path, pos, attributes):
        self.game = game
        self.name = name
        self.path = path
        self.pos = pos
        self.attributes = attributes
        temp_image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(temp_image, (128, 128))


    def draw(self):
        self.game.screen.blit(self.image, self.pos)


    def update(self):
        self.draw()
    

    