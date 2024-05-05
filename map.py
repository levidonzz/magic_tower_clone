import pygame

from setting import *


class Map():
    def __init__(self, game):
        self.game = game
        
    
    def draw(self):
        # for i in range(SCREEN_HEIGHT):
        #     for j in range(SCREEN_WIDTH):
        #         pygame.draw.line(self.game.screen, 'gray', (j ,0), (j, SCREEN_HEIGHT), 1)
        #         j += 20
        #     pygame.draw.line(self.game.screen, 'gray', (0, i), (SCREEN_WIDTH, i), 1)
        #     i += 20
        pygame.draw.line(self.game.screen, 'gray', (0, 80), (SCREEN_WIDTH, 80), 1)
        print("map test")


    def update(self):
        self.draw()