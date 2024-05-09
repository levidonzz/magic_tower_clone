import pygame

from setting import *
from role import Role


class FightPanel():
    def __init__(self, game):
        self.game = game
        self.width = SCREEN_WIDTH // 2
        self.height = SCREEN_HEIGHT // 2
        self.panel = pygame.Surface((FIGHT_PANEL_WIDTH, FIGHT_PANEL_HEIGHT))

    
    def draw(self):
        self.panel.fill('gray')
        dest = (FIGHT_PANEL_POS_X, FIGHT_PANEL_POS_Y)
        temp_player = pygame.image.load('resources/player.png').convert_alpha()
        player = pygame.transform.scale(temp_player, (BLOCK_SIZE * 2, BLOCK_SIZE * 2))

        temp_vsicon = pygame.image.load('resources/vs.png').convert_alpha()
        vs_icon = pygame.transform.scale((temp_vsicon), (BLOCK_SIZE * 2, BLOCK_SIZE * 2))

        panel_rect = self.panel.get_rect()

        blit_sequence = ((player, (panel_rect.left + 100, 150)),
                         (vs_icon, (panel_rect.centerx, 150)),)
        
        self.panel.blits(blit_sequence)

        self.game.screen.blit(self.panel, dest)


    def update(self):
        pass


    def get_monster(self):
        pass