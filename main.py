import pygame
import game_functions as gf
from pygame.sprite import Group

from stats.game_stats import GameStats
from stats.scoreboard import Scoreboard
from settings import Settings
from objects.player import Player
from objects.button import Button


def runGame():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
    player = Player(settings, screen)
    bullets  = Group()
    stones = Group()
    gf.createMultipleStones(settings, screen, player, stones)

    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    pygame.display.set_caption("Hit Stones")
    play_button = Button(screen, "Play")

    while True:
        gf.checkEvents(settings, screen, stats, sb, play_button, player, stones, bullets)

        if stats.game_active:
            player.update()
            gf.updateBullets(settings, screen, stats, sb, player, stones, bullets)
            gf.updateStones(settings, screen, stats, sb, player, stones, bullets)
        
        gf.updateScreen(settings, screen, stats, sb, player, stones, bullets, play_button)


runGame()