import pygame
from pygame.sprite import Sprite

class Rectangle(Sprite):

    def __init__(self, settings, screen, player):
        super(Rectangle, self).__init__() #sprite
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, settings.rectangle_width, settings.rectangle_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        self.y = float(self.rect.y)

        self.color = settings.rectangle_color
        self.speed = settings.rectangle_speed


    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)