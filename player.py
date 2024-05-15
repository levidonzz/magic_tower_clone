import pygame
import time
import random

from setting import *


class Player:
    def __init__(self, game):
        self.game = game
        self.pos_x = INIT_POS_X
        self.pos_y = INIT_POS_Y
        self.health = PLAYER_HEALTH

        self.fight_flag = False
        self.encountered_monster = None

        self.move_delay = 0
        self.move_cooldown = 0.5


    def check_fight(self):
        if self.fight_flag:
            self.fight()


    def fight(self):
        player_damage = random.randint(0, 10)
        monster = self.encountered_monster
        monster.health -= player_damage
        print(f'You dealt {player_damage} to {monster.name}, {monster.name} health: [{monster.health}]')
        time.sleep(1)
        monster_damage = random.randint(0, 15)
        self.health -= monster_damage
        print(f'{monster.name} dealt {monster_damage} to You, Your health [{self.health}]')

        if monster.health <= 0:
            del(self.game.object_handle.monsters[(self.pos_x, self.pos_y)])
            self.fight_flag = False
            self.health = 50
        if self.health <= 0:
            print('You are dead. ----- Game Over -----')
            self.fight_flag = False
            self.health = 50

        
        print('----------------------------------------------')


    def check_monster(self):
        if (self.pos_x, self.pos_y) in self.game.object_handle.monsters.keys():
            self.encountered_monster = self.game.object_handle.monsters[(self.pos_x, self.pos_y)]
            self.fight_flag = True
        else: pass


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
        self.check_monster()
        self.check_fight()