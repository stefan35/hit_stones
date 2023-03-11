import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, settings, screen, player):
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed


    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)