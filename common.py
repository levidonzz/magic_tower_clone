import pygame

from setting import *



def get_player_image():
    i = pygame.image.load('resources/player.png').convert_alpha()
    image = pygame.transform.scale(i, (2 * BLOCK_SIZE, 2 * BLOCK_SIZE))
    return image