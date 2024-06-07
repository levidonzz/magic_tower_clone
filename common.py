import pygame
import random
import time

from setting import *



def get_player_image():
    i = pygame.image.load('resources/player.png').convert_alpha()
    image = pygame.transform.scale(i, (2 * BLOCK_SIZE, 2 * BLOCK_SIZE))
    return image


def get_armament_image(path):
    i = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(i, (BLOCK_SIZE, BLOCK_SIZE))
    return image


def load_iamge(path, width=BLOCK_SIZE, height=BLOCK_SIZE):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image


def set_text(text, size=20, color='black'):
    font = pygame.font.Font(None, size)
    return font.render(str(text), True, color)


def set_random(percentage, number):
    return random.randint(number - number * (percentage // 100), number + number * (percentage // 100))
