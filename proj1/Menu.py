import pygame
import sys

from enum import Enum 

#Enum that represents the game mode of a player
class PlayerMode(Enum):
    HUMAN = 1
    AI_HARD = 2
    AI_MEDIUM = 3
    AI_EASY = 4

pygame.init()

size = (595, 650)
screen = pygame.display.set_mode(size)

font_title = pygame.font.SysFont(None, 50)
font_option = pygame.font.SysFont(None, 30)

"""
Draws the game's main menu on the screen and returns a tuple the game modes chosen
"""
def draw_main_menu():
    menu = font_title.render("WANA", True, (0, 0, 0))
    menu_rect = menu.get_rect(center=(size[0] // 2, 125))

    human_vs_human = font_option.render("Human vs Human", True, (0, 0, 0))
    human_vs_human_rect = human_vs_human.get_rect(center=(size[0] // 2, 275))

    human_vs_ai = font_option.render("Human vs AI", True, (0, 0, 0))
    human_vs_ai_rect = human_vs_ai.get_rect(center=(size[0] // 2, 335))

    ai_vs_ai = font_option.render("AI vs AI", True, (0, 0, 0))
    ai_vs_ai_rect = ai_vs_ai.get_rect(center=(size[0] // 2, 395))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if human_vs_human_rect.collidepoint(event.pos):
                    return (PlayerMode.HUMAN, PlayerMode.HUMAN)
                elif human_vs_ai_rect.collidepoint(event.pos):
                    return (PlayerMode.HUMAN, draw_ai_menu(1))
                elif ai_vs_ai_rect.collidepoint(event.pos):
                    return (draw_ai_menu(1), draw_ai_menu(2))
                
        screen.fill((255, 255, 255))
        # Draw orange boxes around each option
        pygame.draw.rect(screen, (255, 165, 0), human_vs_human_rect, 2)
        pygame.draw.rect(screen, (255, 165, 0), human_vs_ai_rect, 2)
        pygame.draw.rect(screen, (255, 165, 0), ai_vs_ai_rect, 2)

        # Draw blue box around the menu text
        pygame.draw.rect(screen, (0, 0, 255), (menu_rect.left - 10, menu_rect.top - 10,
                                            menu_rect.width + 20, menu_rect.height + 20), 2)

        screen.blit(menu, menu_rect)
        screen.blit(human_vs_human, human_vs_human_rect)
        screen.blit(human_vs_ai, human_vs_ai_rect)
        screen.blit(ai_vs_ai, ai_vs_ai_rect)

        pygame.display.update()

"""
Draws the menu to choose the ai difficulty
"""
def draw_ai_menu(player):
    if(player == 1):
        title = font_title.render("Player 1 AI Difficulty", True, (0, 0, 0))
        title_rect = title.get_rect(center=(size[0] // 2, 100))
    else:
        title = font_title.render("Player 2 AI Difficulty", True, (0, 0, 0))
        title_rect = title.get_rect(center=(size[0] // 2, 100))

    easy_ai = font_option.render("Easy", True, (0, 0, 0))
    easy_ai_rect = easy_ai.get_rect(center=(size[0] // 2, 250))

    medium_ai = font_option.render("Medium", True, (0, 0, 0))
    medium_ai_rect = medium_ai.get_rect(center=(size[0] // 2, 310))

    hard_ai = font_option.render("Hard", True, (0, 0, 0))
    hard_ai_rect = hard_ai.get_rect(center=(size[0] // 2, 370))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_ai_rect.collidepoint(event.pos):
                    return PlayerMode.AI_EASY   
                elif medium_ai_rect.collidepoint(event.pos):
                    return PlayerMode.AI_MEDIUM
                elif hard_ai_rect.collidepoint(event.pos):
                    return PlayerMode.AI_HARD

        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        screen.blit(easy_ai, easy_ai_rect)
        screen.blit(medium_ai, medium_ai_rect)
        screen.blit(hard_ai, hard_ai_rect)

        pygame.display.update()