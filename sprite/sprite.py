import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, name, path, pos):
        self.game = game
        self.name = name
        self.path = path
        self.pos = pos

        self.image = pygame.image.load(path).convert_alpha()


    def draw(self):
        self.game.screen.blit(self.image, self.pos)


    def update(self):
        self.draw()
    

    