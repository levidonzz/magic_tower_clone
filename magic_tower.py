import pygame

from role import Role
from map import Map


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.running = False
        self.dt = 0


    def run(self):
        running = True
        role = Role(self)
        map = Map(self)


        while running:
            self.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            map.update()

            role.update()
            
            pygame.display.flip()
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.clock.tick(15) 


game = Game()
game.run()