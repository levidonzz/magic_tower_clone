import pygame

from setting import *



def get_player_image():
    i = pygame.image.load('resources/player.png').convert_alpha()
    image = pygame.transform.scale(i, (2 * BLOCK_SIZE, 2 * BLOCK_SIZE))
    return image


def get_armament_image(path):
    i = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(i, (BLOCK_SIZE, BLOCK_SIZE))
    return image


def load_iamge(path, width, height):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image