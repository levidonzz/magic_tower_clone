import pygame
import time

from setting import *


class Player:
    def __init__(self, game):
        self.game = game
        self.pos_x = INIT_POS_X
        self.pos_y = INIT_POS_Y
        self.health = PLAYER_HEALTH

        self.fight_flag = False


    def fight(self):
        print('fight is started')
        time.sleep(2)
        print('fight is over, you win')
        self.fight_flag = False


    def check_sprite(self, x, y):
        return (x, y) in self.game.object_handle.monster_pos
    

    def check_sprite_collision(self):
        if self.check_sprite(self.pos_x, self.pos_y):
            self.fight_flag = True
            self.game.fight_panel.draw()
            self.fight()


    def move(self):
        if not self.fight_flag:
            dx, dy = 0, 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                dy -= BLOCK_SIZE
            if keys[pygame.K_a]:
                dx -= BLOCK_SIZE
            if keys[pygame.K_s]:
                dy += BLOCK_SIZE
            if keys[pygame.K_d]:
                dx += BLOCK_SIZE

            self.check_wall_collision(dx, dy)
            

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
        
    
    def check_wall_collision(self, dx, dy):
        next_x = self.pos_x + dx
        next_y = self.pos_y + dy

        grid_x = int(next_x / BLOCK_SIZE)
        grid_y = int(next_y / BLOCK_SIZE)

        if self.check_wall(grid_x, grid_y):
            self.pos_x = next_x
            self.pos_y = next_y

    
    @property
    def pos(self):
        return self.pos_x, self.pos_y


    def update(self):
        self.move()
        self.check_sprite_collision()