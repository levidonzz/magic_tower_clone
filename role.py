import pygame


class Role():
    def __init__(self, screen):
        self.pos_x = 50
        self.pos_y = 10
        self.screen = screen
        self.draw()
    
    def draw(self):
        pygame.draw.circle(self.screen, 'red', (self.pos_x, self.pos_y), 20)


    def update(self):
        self.draw()