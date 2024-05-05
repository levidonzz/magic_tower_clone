import pygame

from role import Role
from map import Map


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.running = False


    def run(self):
        running = True
        role = Role(self.screen)
        map = Map(self)


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill('black')
            role.draw()
            map.update()
            
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000


game = Game()
game.run()