import pygame
import time

from setting import *


class Panel(pygame.Surface):
    def __init__(self, game):
        super().__init__((600, 400))
        self.game = game
        self.pos = (300, 200)


class Merchant(Panel):
    def __init__(self, game):
        super().__init__(game)

    
    def draw(self):
        self.fill('white')

        font = pygame.font.Font(None, 20)
        menu_text = font.render('Menu', True, (0, 0, 0))

        self.blit(menu_text, (100, 50))

        self.game.screen.blit(self, (100, 100))

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