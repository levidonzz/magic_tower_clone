import pygame

from setting import *


class Button(pygame.Surface):
    def __init__(self, game):
        super().__init__((40, 20))
        self.game = game
        self.rect = self.get_rect()
        self.fill('gray')
        image = pygame.image.load('resources/buy.png')
        self.blit(image, (0, 0))



    def is_clicked(self, pos):
        return self.rect(pos)
    

    def click(self):
        if self.is_clicked(pygame.mouse.get_pos()):
            print('shoped')