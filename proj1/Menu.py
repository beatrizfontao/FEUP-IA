import pygame
import sys

from enum import Enum


class PlayerMode(Enum):
    HUMAN = 1
    AI_HARD = 2
    AI_MEDIUM = 3
    AI_EASY = 4


pygame.init()

size = (595, 600)
screen = pygame.display.set_mode(size)

font_title = pygame.font.SysFont(None, 50)
font_option = pygame.font.SysFont(None, 30)

def draw_main_menu():
    menu = font_title.render("Menu", True, (0, 0, 0))
    menu_rect = menu.get_rect(center=(size[0] // 2, 100))

    human_vs_human = font_option.render("Human vs Human", True, (0, 0, 0))
    human_vs_human_rect = human_vs_human.get_rect(center=(size[0] // 2, 250))

    human_vs_ai = font_option.render("Human vs AI", True, (0, 0, 0))
    human_vs_ai_rect = human_vs_ai.get_rect(center=(size[0] // 2, 310))

    ai_vs_ai = font_option.render("AI vs AI", True, (0, 0, 0))
    ai_vs_ai_rect = ai_vs_ai.get_rect(center=(size[0] // 2, 370))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        screen.blit(menu, menu_rect)
        screen.blit(human_vs_human, human_vs_human_rect)
        screen.blit(human_vs_ai, human_vs_ai_rect)
        screen.blit(ai_vs_ai, ai_vs_ai_rect)

        pygame.display.update()


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

draw_main_menu()
