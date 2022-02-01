import pygame
from pygame.sprite import Sprite

class Stone(Sprite):

    def __init__(self, settings, screen):
        super(Stone, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images\stone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        
        #self.angle = 0.1
        #self.rect = pygame.rect.Rect((10, 10, 40, 40))
        #rotated_image = pygame.transform.rotate(self.image, 1)
        #new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
        #self.rect = rotated_image.get_rect(center = self.image.get_rect(center = (0, 0)).center)
        
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


    """
    def draw(self): 
        print('this is it')
        self.rotated_image = pygame.transform.rotate(self.image, self.angle )
        pos_rect_rot = self.rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(self.rotated_image, pos_rect_rot)

        self.angle += 0.1
    """

