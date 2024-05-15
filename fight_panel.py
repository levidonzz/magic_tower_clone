import pygame

from setting import *


class FightPanel(pygame.Surface):
    def __init__(self, game):
        pygame.Surface.__init__(self, (600, 400))
        self.game = game
        self.x = 300
        self.y = 200
        

    def draw(self):
        self.fill('gray')
        player = self.game.player
        

        self.game.screen.blit(self, (self.x, self.y))