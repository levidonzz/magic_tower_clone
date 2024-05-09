import pygame

from role import Role
from map import Map
from setting import *
from sprite.sprite import Monster
from fight_panel import FightPanel


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.running = False
        self.dt = 0


    def draw(self):
        # dest = (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200)
        # monster = Monster(self, 'test_monster', 'resources/house.png', dest)
        # monster.draw()
        pass
        

    def run(self):
        running = True
        role = Role(self, 'Joe', 'resources/player.png')
        map = Map(self)
        all_sprites = pygame.sprite.Group()
        fight_panel = FightPanel(self)

        # init monster
        attributes = {
            "health": 100,
        }
        temp_monster = pygame.image.load('resources/house.png').convert_alpha()
        monster_image = pygame.transform.scale((temp_monster), (BLOCK_SIZE * 2, BLOCK_SIZE * 2))
        monster = Monster(game, 'yaoguai', 'resources/house.png', (fight_panel.panel.get_rect().right - 100, 150), attributes)

        while running:
            self.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            map.update()
            role.update()
            self.draw()
            monster.draw()
            fight_panel.draw()
            all_sprites.update()
            all_sprites.draw(self.screen)
            
            pygame.display.flip()
            pygame.display.set_caption(str(self.clock.get_fps()))
            
            role.fight(monster)
            self.clock.tick(15) 


game = Game()
game.run()