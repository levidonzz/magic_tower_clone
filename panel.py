import pygame
import time

from setting import *
from button import Button
from common import *


class Panel(pygame.Surface):
    def __init__(self, game):
        super().__init__((600, 400))
        self.game = game
        self.pos = (300, 200)

    
    def draw(self, surface):
        self.game.screen.blit(surface, self.pos)


class PlayerInfo(pygame.Surface):
    def __init__(self, game):
        super().__init__((200, 1000))
        self.game = game
        self.pos = (1000, 0)

    def draw(self):
        self.fill('white')
        font = pygame.font.Font(None, 30)

        player_image = get_player_image()
        self.blit(player_image, (1 * BLOCK_SIZE, 2 * BLOCK_SIZE))

        gold_image = load_iamge('resources/gold.png', 80, 40)
        health_image = load_iamge('resources/health.png', 80, 40)
        attack_image = load_iamge('resources/attack.png', 80, 40)
        defense_image = load_iamge('resources/defense.png', 80, 40)
        buy_image = load_iamge('resources/buy.png', 40, 20)
        vs_image = load_iamge('resources/vs.png', 60, 30)

        player = self.game.player

        gap = 20
        gold = font.render(str(player.gold), True, 'black')
        health = font.render(str(player.health), True, 'black')
        attack = font.render(str(player.attack), True, 'black')
        defense = font.render(str(player.defense), True, 'black')

        self.blit(gold_image, (20, 5 * BLOCK_SIZE))
        self.blit(gold, (110, 5 * BLOCK_SIZE + 10))

        self.blit(health_image, (20, 7 * BLOCK_SIZE + gap))
        self.blit(health, (110, 7 * BLOCK_SIZE + gap + 10))

        self.blit(attack_image, (20, 8 * BLOCK_SIZE + gap))
        self.blit(attack, (110, 8 * BLOCK_SIZE + gap + 10))

        self.blit(defense_image, (20, 9 * BLOCK_SIZE + gap))
        self.blit(defense, (110, 9 * BLOCK_SIZE + gap + 10))


        armaments = self.game.player.armaments
        if armaments:
            i = 0
            for armament in armaments.values():
                name, path, value, amount, sort, attribute = armament.get()
                image = get_armament_image(path)
                self.blit(image, (i * BLOCK_SIZE, 12 * BLOCK_SIZE))
                i += 1.5

        self.game.screen.blit(self, self.pos)


class Merchant(Panel):
    def __init__(self, game):
        super().__init__(game)
        self.button = Button(self.game)
        self.buttones = {}
        self.shop_open = False


    def sell(self, player, item_index):
        pass
    
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
            self.blit(self.button, (init_pos_x, 280))
            button = pygame.Rect(init_pos_x + 300, 280 + 200, BLOCK_SIZE, BLOCK_SIZE // 2)
            self.buttones[key] = button
            if key in self.game.player.purchased_items:
                button = Button(self.game, 'black')
                self.blit(button, (init_pos_x, 280))

            quit_image = pygame.image.load('resources/quit.png')
            self.buttones['quit'] = pygame.Rect(480 + 300, 320 + 200, 80, 40)
            self.blit(quit_image, (480, 320))
            init_pos_x += delta_pos_x

        super().draw(self)
        

class FightPanel(Panel):
    def __init__(self, game):
        super().__init__(game)

    
    def draw(self):

        self.fill('gray')
        player = self.game.player
        monster = self.game.player.encountered_monster

        player_image = get_player_image()
        monster_image = load_iamge(monster.path, 2 * BLOCK_SIZE, 2 * BLOCK_SIZE)
        heart_image = load_iamge('resources/heart.png')
        vs_image = load_iamge('resources/vs.png', 120, 60)

        font = pygame.font.Font(None, 30)

        player_health = font.render(str(player.health), True, (0, 0, 0))
        monster_health = font.render(str(player.encountered_monster.health), True, (0, 0, 0))

        player_fight_text = font.render(str(f'[{player.player_damage}] for {monster.name}'), True, (0, 0, 0))
        monster_fight_text = font.render(str(f'[{player.monster_damage}] for You'), True, (0, 0, 0))

        time.sleep(1)
        
        self.blit(player_image, (100, 100))
        self.blit(heart_image, (100, 220))
        self.blit(player_health, (150, 230))
        self.blit(vs_image, (240, 100))
        self.blit(monster_image, (420, 100))
        self.blit(heart_image, (420, 220))
        self.blit(monster_health, (470, 230))

        self.blit(player_fight_text, (200, 300))
        self.blit(monster_fight_text, (200, 350))

        if self.game.player.health <= 0:
            game_over_text = set_text('Your health is zone, You die. Game over')
            self.blit(game_over_text, (250, 300))
        elif self.game.player.encountered_monster.health <= 0:
            monster_die_text = set_text('The monster is die, You won')
            self.blit(monster_die_text, (250, 300))

        super().draw(self)