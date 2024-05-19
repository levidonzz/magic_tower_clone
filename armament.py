import pygame


class Armanent:
    def __init__(self, game, name, path, value, amount, sort):
        self.game = game
        self.name = name
        self.value = value
        self.amount = amount
        self.sort = sort
        self.path = path


class Weapon(Armanent):
    def __init__(self, game, name, path, value, amount, sort, hurt):
        super().__init__(game, name, path, value, amount, sort)
        self.hurt = hurt


class Armor(Armanent):
    def __init__(self, game, name, path, value, amount, sort, defense):
        super().__init__(game, name, path, value, amount, sort)
        self.defense = defense
