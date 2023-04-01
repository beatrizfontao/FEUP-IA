import pygame, sys
from State import State
from View import View
from Minimax import *

from Menu import *

pygame.init()

#Screen and Background
screen = pygame.display.set_mode((595, 600))
background = pygame.image.load("a.png")

def draw(state, board, display):
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    board.draw_board(state, display)
    pygame.display.update()

def human_turn(state, board):
    print('turn')    
    while True:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(pos)
                    board.handle_click(pos, state)
                    break

def game(playerMode):
    state = State(9)
    print('state')
    board = View(9, state.board)
    print('board')
    draw(state, board, screen)
    while True:
        print('while')
        cur_turn = 0 if state.turn == 1 else 1
        match playerMode[cur_turn]:
            case PlayerMode.HUMAN:
                print('player 1 turn')
                human_turn(state, board)
                print('end player 1 turn')
            case PlayerMode.AI_EASY:
                execute_minimax_move(board, num_enemy_moves, 3)
            case PlayerMode.AI_MEDIUM:
                print('ai medium')
            case PlayerMode.AI_HARD:
                print('ai hard')

        i = state.is_game_over()
        if i != 0:
            print("player " + str(i) + " won!")
            sys.exit()
        draw(state, board, screen)

gameMode = draw_main_menu()
print(gameMode)
game(gameMode)
