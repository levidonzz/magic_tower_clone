import pygame

from role import Role
from map import Map
from setting import *
from sprite.sprite import Monster


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.running = False
        self.dt = 0


    def draw(self):
        dest = (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200)
        monster = Monster(self, 'test_monster', 'resources/house.png', dest)

        monster.draw()

    def run(self):
        running = True
        role = Role(self)
        map = Map(self)
        all_sprites = pygame.sprite.Group()

        while running:
            self.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            map.update()
            role.update()
            self.draw()

            all_sprites.update()
            all_sprites.draw(self.screen)
            
            pygame.display.flip()
            pygame.display.set_caption(str(self.clock.get_fps()))
            self.clock.tick(15) 


game = Game()
game.run()