import pygame
from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self, settings, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images\player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        #self.rect = pygame.rect.Rect((10, 10, 40, 40))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 6
        self.center = float(self.rect.centerx)

        self.move_right = False
        self.move_left = False


    def centerPlayer(self):
        self.center = self.screen_rect.centerx


    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.player_speed
        elif self.move_left and self.rect.left > 0:
            self.center -= self.settings.player_speed
        
        self.rect.centerx = self.center


    def draw(self):
        #pygame.draw.rect(self.screen, (0, 0, 128), self.rect)
        self.screen.blit(self.image, self.rect)