import pygame

from sprite import Monster


class ObjectHandle:
    def __init__(self, game):
        self.game = game
        self.monster_path = 'resources/monsters/'
        self.monster_group = pygame.sprite.Group()
        self.monster_pos = []

    
    def add_monster(self):
        self.monster_group.add(Monster(self.game, self.monster_path + 'dog1.png', (200, 200), 'Dog1'))
        self.monster_group.add(Monster(self.game, self.monster_path + 'dog2.png', (400, 200), 'Dog2'))


    def update(self):
        self.add_monster()
        self.get_sprite_pos()

    
    def get_sprite_pos(self):
        for monster in self.monster_group.sprites():
            self.monster_pos.append(monster.rect)