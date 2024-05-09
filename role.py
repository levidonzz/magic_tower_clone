import pygame
import time
import random

from setting import *
from map import Map


class Role():
    def __init__(self, game, name, path):
        self.pos_x = 120
        self.pos_y = 120
        self.game = game
        self.name = name
        self.path = path
        self.draw()
        self.map = Map(game)

        # player attributes
        self.health = HEALTH

    
    def fight(self, monster):
        while True:
            if self.health <= 0:
                print(f"You are been defeated by [{monster.name}]")
                break
            if monster.attributes["health"] <= 0:
                print(f"You are been defeated the monster [{monster.name}]")
                break

            player_hurt = random.randint(0, 10)
            monster.attributes["health"] -= player_hurt
            print(f"You dealt {player_hurt} damage to {monster.name}")

            time.sleep(0.5)

            monster_hurt = random.randint(0, 10)
            self.health -= monster_hurt
            print(f"{monster.name} dealth {monster_hurt} damage to You")


    def draw(self):
        temp_player = pygame.image.load(self.path).convert_alpha()
        player = pygame.transform.scale(temp_player, (BLOCK_SIZE, BLOCK_SIZE))
        pos = (self.pos_x, self.pos_y)
        self.game.screen.blit(player, pos)


    def get_player(self):
        temp_player = pygame.image.load(self.path).convert_alpha()
        player = pygame.transform.scale(temp_player, (BLOCK_SIZE, BLOCK_SIZE))
        return player

    
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
