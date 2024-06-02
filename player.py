import pygame
import time
import random

from setting import *
from sprite import Monster, Merchant
from armament import Weapon, Armor


class Player:
    def __init__(self, game):
        self.game = game
        self.pos_x = INIT_POS_X
        self.pos_y = INIT_POS_Y
        self.health = PLAYER_HEALTH
        self.gold = 100
        self.attack = 10
        self.defense = 5

        self.fight_flag = False
        self.encountered_flag = False
        self.encountered_monster = None
        self.player_damage = None
        self.monster_damage = None


        self.move_delay = 0
        self.move_cooldown = 0.5

        self.armaments = {}
        self.purchased_items = {}

    
    def check_buy(self):
        buttons = self.game.merchant_panel.buttones
        for button, rect in buttons.items():
            if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed().index(0) == 1:
                if button == 'quit':
                    self.encountered_flag = False
                    self.pos_x += BLOCK_SIZE
                    return
                if button not in self.purchased_items:
                    self.buy(button)
            

    
    def buy(self, armament_name):
        armament = self.game.object_handle.armaments[armament_name]
        if armament:
            name, path, value, amount, sort, attribute = armament.get()
            if self.gold >= value and name not in self.purchased_items:
                self.gold -= value
                self.armaments[name] = armament
                if attribute == 'weapon':
                    amount -= 1
                    self.armaments[name] = Weapon(self.game, name,  path, value, amount, sort, attribute)
                elif attribute == 'armor':
                    amount -= 1
                    self.armaments[name] = Armor(self.game, name,  path, value, amount, sort, attribute)
                self.purchased_items[name] = True
                self.update_attribute(armament)

            elif self.gold < value:
                print('money is less')
        
        
    def check_collision(self):
        if (self.pos_x, self.pos_y) in self.game.object_handle.barriers.keys():
            obj = self.game.object_handle.barriers[(self.pos_x, self.pos_y)]
            if isinstance(obj, Monster):
                self.encountered_monster = obj
                self.fight_flag = True
                self.fight()
            elif isinstance(obj, Merchant):
                self.encountered_flag = True
                # print('encountered merchant...')
        else:
            # print('not encountered')
            pass


    def fight(self):
        monster = self.encountered_monster

        if self.health <= 0:
            self.fight_flag = False
            return
        if monster.health <= 0:
            del(self.game.object_handle.barriers[(self.pos_x, self.pos_y)])
            self.game.object_handle.monster_group.remove(monster)
            self.fight_flag = False
            self.health = PLAYER_HEALTH
            return
        
        self.player_damage = self.attack + monster.defense
        self.monster_damage = monster.attack + self.defense
        monster.health -= self.player_damage
        self.health -= self.monster_damage


    def move(self):
        if not self.fight_flag or not self.encountered_flag:
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
    

    def update_attribute(self, armament):
            name, path, value, amount, sort, attribute = armament.get()
            if sort == 'weapon':
                self.attack += attribute
            elif sort == 'armor':
                self.defense += attribute


    def update(self):
        self.move()
        self.check_collision()
        self.check_buy()

