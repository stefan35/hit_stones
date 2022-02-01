import sys
import pygame
from time import sleep

from objects.rectangle import Rectangle
from objects.stone import Stone

def checkEvents(settings, screen, stats, sb, play_button, player, stones, rectangles):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                checkKeyDownEvents(event, settings, screen, player, rectangles)
            elif event.type == pygame.KEYUP:
                checkKeyUpEvents(event, player)
            elif event.type == pygame.K_q:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                checkPlayButton(settings, screen, stats, sb, play_button, player, stones, rectangles, mouse_x, mouse_y)


def checkKeyDownEvents(event, settings, screen, player, rectangles):
    if event.key == pygame.K_RIGHT:
        player.move_right = True
    elif event.key == pygame.K_LEFT:
        player.move_left = True
    elif event.key == pygame.K_SPACE:
        createRectangle(settings, screen, player, rectangles)
              

def checkKeyUpEvents(event, player):
    if event.key == pygame.K_RIGHT:
        player.move_right = False
    elif event.key == pygame.K_LEFT:
        player.move_left = False


def checkPlayButton(settings, screen, stats, sb, play_button, player, stones, rectangles, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if button_clicked and not stats.game_active:
        settings.initializeDynamiSettings()
        pygame.mouse.set_visible(False)
        
        stats.resetStats()
        stats.game_active = True

        sb.prepScore()
        sb.prepHighScore()
        sb.prepLevel()
        sb.prepPlayer()

        stones.empty()
        rectangles.empty()

        createMultipleStones(settings, screen, player, stones)
        player.centerPlayer()


def getNumberRows(settings, player_height, stone_height):
    available_space_y = (settings.screen_height - (6 * stone_height) - player_height)
    number_rows = int(available_space_y / (2 * stone_height))
    
    return number_rows


def createStone(settings, screen, stones, stone_number, row_number):
    stone = Stone(settings, screen)
    stone_width = stone.rect.width
    stone.x = stone_width + 2 * stone_width * stone_number
    stone.rect.x = stone.x
    stone.rect.y = 2.5 * stone.rect.height + 2 * stone.rect.height * row_number
    stones.add(stone)


def createMultipleStones(settings, screen, player, stones):
    stone = Stone(settings, screen)
    stone_width = stone.rect.width
    
    available_space_x = settings.screen_width - (2 * stone_width)
    number_stone_x = int(available_space_x / (2 * stone_width))
    number_rows = getNumberRows(settings, player.rect.height, stone.rect.height)

    for row_number in range(number_rows):
        for stone_number in range(number_stone_x):
            createStone(settings, screen, stones, stone_number, row_number)


def changeStoneDirection(settings, stones):
    for stone in stones.sprites():
        stone.rect.y += settings.stones_drop_speed
    settings.stones_direction *= -1


def checkStonesEdges(settings, stones):
    for stone in stones.sprites():
        if stone.checkEdges():
            changeStoneDirection(settings, stones)
            break


def checkStonesBottom(settings, screen, stats, sb, player, stones, rectangles):
    screen_rect = screen.get_rect()
    
    for stone in stones.sprites():
        if stone.rect.bottom >= screen_rect.bottom:
            playerHit(settings, screen, stats, sb, player, stones, rectangles)
            break


def updateStones(settings, screen, stats, sb, player, stones, rectangles):
    checkStonesEdges(settings, stones)
    stones.update()

    if pygame.sprite.spritecollideany(player, stones):
        playerHit(settings, screen, stats, sb, player, stones, rectangles)
    
    checkStonesBottom(settings, screen, stats, sb, player, stones, rectangles)


def checkCollisions(settings, screen, stats, sb, player, stones, rectangles):
    collisions = pygame.sprite.groupcollide(rectangles, stones, True, True)

    if collisions:
        for stone in collisions.values():
            stats.score += settings.stone_points * len(stones)
            sb.prepScore()
        checkHighScore(stats, sb)

    if len(stones) == 0:
        rectangles.empty()
        
        settings.increaseSpeed()
        stats.level += 1
        sb.prepLevel()

        createMultipleStones(settings, screen, player, stones)


def updateRectangles(settings, screen, stats, sb, player, stones, restangles):
    restangles.update()

    for rectangle in restangles.copy():
        if rectangle.rect.bottom <= 0:
            restangles.remove(rectangle)
    
    checkCollisions(settings, screen, stats, sb, player, stones, restangles)  


def createRectangle(settings, screen, player, rectangles):
    if len(rectangles) < settings.rectangles_allowed:
        new_rectangle = Rectangle(settings, screen, player)
        rectangles.add(new_rectangle) 


def playerHit(settings, screen, stats, sb, player, stones, rectangles):
    if stats.player_left > 0:
        stats.player_left -= 1

        sb.prepPlayer()
        stones.empty()
        rectangles.empty()

        createMultipleStones(settings, screen, player, stones)
        player.centerPlayer()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def checkHighScore(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))
        
        sb.prepHighScore()


def updateScreen(settings, screen, stats, sb, player, stones, rectangles, play_button):
    screen.fill(settings.bg_color)

    for rectangle in rectangles:
        rectangle.draw()
    
    player.draw()
    stones.draw(screen)
    sb.showScore()

    if not stats.game_active:
        if stats.player_left == 0:
            play_button.prepMsg("Try again")
        play_button.drawButton()

    pygame.display.flip()