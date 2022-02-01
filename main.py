import pygame
import game_functions as gf
from pygame.sprite import Group

from stats.game_stats import GameStats
from stats.scoreboard import Scoreboard
from settings import Settings
from objects.player import Player
from button import Button

def runGame():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
    player = Player(settings, screen)
    rectangles  = Group()
    stones = Group()
    gf.createMultipleStones(settings, screen, player, stones)

    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    pygame.display.set_caption("Hit Stones")
    play_button = Button(screen, "Play")

    while 1:
        gf.checkEvents(settings, screen, stats, sb, play_button, player, stones, rectangles)

        if stats.game_active:
            player.update()
            gf.updateRectangles(settings, screen, stats, sb, player, stones, rectangles)
            gf.updateStones(settings, screen, stats, sb, player, stones, rectangles)
        
        gf.updateScreen(settings, screen, stats, sb, player, stones, rectangles, play_button)


runGame()

"""
pip install pyinstaller

cd YourFilePath

pyinstaller --onefile YourFileName
"""