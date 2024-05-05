import pygame

from setting import *


class Role():
    def __init__(self, game):
        self.pos_x = 120
        self.pos_y = 120
        self.game = game
        self.draw()
    

    def draw(self):
        pygame.draw.rect(self.game.screen, 'red', (self.pos_x, self.pos_y, BLOCK_SIZE, BLOCK_SIZE), BLOCK_SIZE)

    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos_x -= BLOCK_SIZE
        if keys[pygame.K_RIGHT]:
            self.pos_x += BLOCK_SIZE
        if keys[pygame.K_UP]:
            self.pos_y -= BLOCK_SIZE
        if keys[pygame.K_DOWN]:
            self.pos_y += BLOCK_SIZE


    def check_collide(self):
        pass


    def update(self):
        self.draw()
        self.move()
