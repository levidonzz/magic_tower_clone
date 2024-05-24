import pygame
import time

from setting import *


class Panel(pygame.Surface):
    def __init__(self, game):
        super().__init__((600, 400))
        self.game = game
        self.pos = (300, 200)

    
    def draw(self, surface):
        self.game.screen.blit(surface, self.pos)


class Merchant(Panel):
    def __init__(self, game):
        super().__init__(game)
    
    
    def draw(self):
        self.fill('white')

        font = pygame.font.Font(None, 20)

        armaments = self.game.object_handle.armaments
        delta_pos_x = 150
        init_pos_x = 100
        for key, value in armaments.items():
            name, path, value, amount, sort, _ = value.get()
            image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (BLOCK_SIZE, BLOCK_SIZE))
            armament_name = font.render(name, True, 'black')
            value = font.render(str(value), True, 'black')
            self.blit(armament_name, (init_pos_x, 180))
            self.blit(image, (init_pos_x, 200))
            self.blit(value, (init_pos_x, 250))
            init_pos_x += delta_pos_x

        print('-------------------------')
        super().draw(self)
        

class FightPanel(Panel):
    def __init__(self, game):
        super().__init__(game)

    
    def draw(self):

        self.fill('gray')
        player = self.game.player
        monster = self.game.player.encountered_monster

        player_image = pygame.transform.scale(pygame.image.load('resources/player.png').convert_alpha(), (BLOCK_SIZE, BLOCK_SIZE))
        monster_image = pygame.transform.scale(pygame.image.load(monster.path).convert_alpha(), (BLOCK_SIZE, BLOCK_SIZE))
        heart_image = pygame.image.load('resources/heart.png').convert_alpha()
        vs_image = pygame.image.load('resources/vs.png').convert_alpha()

        font = pygame.font.Font(None, 20)

        player_health = font.render(str(f'Your Health: {player.health}'), True, (0, 0, 0))
        monster_health = font.render(str(f'Monster Health: {player.encountered_monster.health}'), True, (0, 0, 0))

        player_fight_text = font.render(str(f'[{player.player_damage}] for {monster.name}'), True, (0, 0, 0))
        monster_fight_text = font.render(str(f'[{player.monster_damage}] for You'), True, (0, 0, 0))

        time.sleep(1)

        self.blit(player_fight_text, (150, 300))
        self.blit(monster_fight_text, (150, 330))

        self.blit(player_health, (200 - BLOCK_SIZE, 250))
        self.blit(monster_health, (400 - BLOCK_SIZE, 250)) 

        self.blit(player_image, (200 - BLOCK_SIZE, 150))
        self.blit(monster_image, (400 - BLOCK_SIZE, 150))
        self.blit(heart_image, (200 - BLOCK_SIZE, 200))
        self.blit(heart_image, (400 - BLOCK_SIZE, 200))
        self.blit(vs_image, (300 - BLOCK_SIZE, 150))

        super().draw(self)    