import pygame


class Armanent:
    def __init__(self, game, name, value):
        self.game = game
        self.name = name
        self.value = value


class Weapon(Armanent):
    def __init__(self, hurt):
        super.__init__(self)
        self.hurt = hurt


class Armor(Armanent):
    pass
