import pygame

from setting import *
from map import Map


class Role():
    def __init__(self, game):
        self.pos_x = 120
        self.pos_y = 120
        self.game = game
        self.draw()
        self.map = Map(game)
    

    def draw(self):
        pygame.draw.rect(self.game.screen, 'red', (self.pos_x, self.pos_y, BLOCK_SIZE, BLOCK_SIZE), BLOCK_SIZE)

    
    def move(self):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= BLOCK_SIZE
        if keys[pygame.K_RIGHT]:
            dx += BLOCK_SIZE
        if keys[pygame.K_UP]:
            dy -= BLOCK_SIZE
        if keys[pygame.K_DOWN]:
            dy += BLOCK_SIZE
        
        self.check_wall_collision(dx, dy)


    def check_wall(self, x, y):
        flag = (x, y) not in self.map.world_map
        print(flag)
        return flag
        
    
    def check_wall_collision(self, dx, dy):
        next_x = self.pos_x + dx
        next_y = self.pos_y + dy

        grid_x = int(next_x / BLOCK_SIZE)
        grid_y = int(next_y / BLOCK_SIZE)

        if self.check_wall(grid_x, grid_y):
            self.pos_x = next_x
            self.pos_y = next_y


    def update(self):
        self.draw()
        self.move()
