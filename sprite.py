import pygame
import random

from setting import *


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, path, pos, name, health, attack=10, defense=10, value=10):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.path = path
        self.rect = pos
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.value = value
        self.image = self.get_image()


    def get_image(self):
        image = pygame.image.load(self.path).convert_alpha()
        image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))
        return image
    

    def get_attack(self):
        attack = random.randint(self.attack - self.attack // 5, self.attack + self.attack * 0.2)
        return attack


    def update(self):
        pass


class Merchant(pygame.sprite.Sprite):
    def __init__(self, game, path, pos, name):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.path = path
        self.rect = pos
        self.name = name
        self.image = self.get_image()
        self.commodity = {}
        self.overage = OVERAGE

    
    def get_image(self):
        image = pygame.image.load(self.path).convert_alpha()
        image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))
        return image
    

    def sell(self, goods):
        if goods.name in self.commodity.keys():
            self.overage += goods.value
            del(self.commodity[goods.name])