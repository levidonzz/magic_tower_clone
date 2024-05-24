import pygame

from sprite import Monster, Merchant
from armament import *


class ObjectHandle:
    def __init__(self, game):
        self.game = game
        self.monster_path = 'resources/monsters/'
        self.armament_path = 'resources/'
        self.monster_group = pygame.sprite.Group()
        self.merchant_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.armor_group = pygame.sprite.Group()
        self.monsters = {}
        self.monster_pos = []
        self.current_monster = None

        self.barriers = {}
        self.armaments = {}

        self.add_monster()
        self.get_sprite_pos()
        self.add_merchant()
        self.add_armament()

    
    def add_monster(self):
        monster_data = [
            (self.monster_path + 'dog1.png', (200, 200), 'Dog1', 20),
            (self.monster_path + 'dog2.png', (400, 200), 'Dog2', 50),
        ]
        for path, pos, name, health in monster_data:
            monster = Monster(self.game, path, pos, name, health)
            self.monster_group.add(monster)
            self.barriers[pos] = monster
            self.monsters[pos] = monster

    
    def get_sprite_pos(self):
        for monster in self.monster_group.sprites():
            self.monster_pos.append(monster.rect)

    
    def add_merchant(self):
        pos = (320, 320)
        merchant = Merchant(self.game, 'resources/fire2.jpg', pos, 'Merchant')
        self.merchant_group.add(merchant)
        self.barriers[pos] = merchant


    def add_armament(self):
        armaments_data = [
            ('one sword', self.armament_path + 'one_sword.png', 10, 2, 'weapon', 10),
            ('two sword', self.armament_path + 'two_sword.png', 10, 2, 'weapon', 15),
            ('shield', self.armament_path + 'shield.png', 10, 2, 'armor', 20),
        ]
        
        for armament in armaments_data:
            name, path, value, amount, sort, attribute = armament
            if sort == 'weapon':
                weapon = Weapon(self.game, name, path, value, amount, sort, attribute)
                # self.weapon_group.add(weapon)
                self.armaments[name] = weapon
            elif sort == 'armor':
                armor = Armor(self.game, name, path, value, amount, sort, attribute)
                # self.armor_group.add(armor)
                self.armaments[name] = armor
