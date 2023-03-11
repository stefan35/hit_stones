import pygame.font
from pygame.sprite import Group

from objects.player import Player


class Scoreboard():

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prepScore()
        self.prepHighScore()
        self.prepLevel()
        self.prepPlayer()

    
    def prepScore(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 3
    

    def prepHighScore(self):
        high_score = int(round(self.stats.high_score))
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    

    def prepLevel(self):
        self.level_img = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = 50
    

    def prepPlayer(self):
        self.players = Group()

        for player_number in range(self.stats.player_left):
            player = Player(self.settings, self.screen)
            player.rect.x = 10 + player_number * player.rect.width
            player.rect.y = 10
            self.players.add(player)
    

    def showScore(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.players.draw(self.screen)