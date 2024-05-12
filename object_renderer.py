import pygame

from setting import *
from map import MINI_MAP

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.wall_texture = self.load_wall_textures()


    def draw(self):
        self.draw_map()
        self.draw_player()
        self.draw_sprites()


    def draw_map(self):
        textures = self.load_wall_textures()
        for j, row in enumerate(MINI_MAP):
            for i, _ in enumerate(row):
                if MINI_MAP[j][i] == False:
                    self.game.screen.blit(textures[0], (i * BLOCK_SIZE, j * BLOCK_SIZE))
                if MINI_MAP[j][i] == 1:
                    self.game.screen.blit(textures[1], (i * BLOCK_SIZE, j * BLOCK_SIZE))
                if MINI_MAP[j][i] == 2:
                    self.game.screen.blit(textures[2], (i * BLOCK_SIZE, j * BLOCK_SIZE))



    def draw_player(self):
        player_image = self.get_texture('resources/player.png', (BLOCK_SIZE, BLOCK_SIZE))
        player_pos = (self.game.player.pos_x, self.game.player.pos_y)
        self.game.screen.blit(player_image, player_pos)


    def draw_sprites(self):
        monster_group = self.game.object_handle.monster_group
        monster_group.draw(self.game.screen)
        # for monster in monster_group:
        #     self.game.screen.blit(monster.image, monster.pos)


    @staticmethod
    def get_texture(path, res=(BLOCK_SIZE, BLOCK_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)
    

    def load_wall_textures(self):
        return {
            0: self.get_texture('resources/floor.jpg'),
            1: self.get_texture('resources/mosaic1.jpg'),
            2: self.get_texture('resources/fire2.jpg'),
        }