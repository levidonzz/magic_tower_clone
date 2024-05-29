import pygame


class Armanent:
    def __init__(self, game, name, path, value, amount, sort):
        self.game = game
        self.name = name
        self.value = value
        self.amount = amount
        self.sort = sort
        self.path = path

    
    def get(self):
        return self.name, self.path, self.value, self.amount, self.sort


class Weapon(Armanent):
    def __init__(self, game, name, path, value, amount, sort, hurt):
        super().__init__(game, name, path, value, amount, sort)
        self.hurt = hurt

    
    def get(self):
        return self.name, self.path, self.value, self.amount, self.sort, self.hurt        


class Armor(Armanent):
    def __init__(self, game, name, path, value, amount, sort, defense):
        super().__init__(game, name, path, value, amount, sort)
        self.defense = defense
    
    
    def get(self):
        return self.name, self.path, self.value, self.amount, self.sort, self.defense

