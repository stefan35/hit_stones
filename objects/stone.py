import pygame
from pygame.sprite import Sprite

class Stone(Sprite):

    def __init__(self, settings, screen):
        super(Stone, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images\stone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def checkEdges(self):
        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += (self.settings.stone_speed * self.settings.stones_direction)
        self.rect.x = self.x