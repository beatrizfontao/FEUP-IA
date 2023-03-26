import pygame, sys
from Board import Board

from Menu import *

pygame.init()

#Screen and Background
screen = pygame.display.set_mode((595, 600))
background = pygame.image.load("a.png")

def draw(board, display):
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    board.draw(display)
    pygame.display.update()

#board.get_valid_moves('player1')

def human_turn(board):
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.handle_click(pos)

def game(playerMode):
    board = Board(9)

    while True:
        cur_turn = 0 if board.turn == 'player1' else 1
        match playerMode[cur_turn]:
            case PlayerMode.HUMAN:
                human_turn(board)
            case PlayerMode.AI_EASY:
                print('ai easy')
            case PlayerMode.AI_MEDIUM:
                print('ai medium')
            case PlayerMode.AI_HARD:
                print('ai hard')

        i = board.is_game_over()
        if i != 0:
            print("player " + str(i) + " won!")
            sys.exit()
        draw(board, screen)

gameMode = draw_main_menu()
print(gameMode)
game(gameMode)