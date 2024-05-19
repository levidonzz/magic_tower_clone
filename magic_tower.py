import pygame
import sys

from map import Map
from player import Player
from setting import *
from object_renderer import ObjectRenderer
from object_handle import ObjectHandle
# from fight_panel import FightPanel

from panel import FightPanel, Merchant


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.running = False
        self.dt = 0

        self.new_game()

    
    def new_game(self):
        self.map = Map(self)
        self.object_handle = ObjectHandle(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.fight_panel = FightPanel(self)
        self.merchant_panel = Merchant(self)

    
    def update(self):
        self.map.update()
        self.player.update()

        # self.object_handle.update()
        self.clock.tick(60)
        pygame.display.flip()
        pygame.display.set_caption(f"{self.clock.get_fps() :.1f}")

    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        
    def draw(self):
        self.object_renderer.draw()
                
        
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            if self.player.fight_flag:
                self.fight_panel.draw()
            elif self.player.encountered_flag:
                self.merchant_panel.draw()

            self.dt = self.clock.tick(60) / 1000


game = Game()
game.run()