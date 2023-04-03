import pygame, sys, time
from State import State
from View import View
from NewMinimax import *

from Menu import *

pygame.init()

#Screen and Background
screen = pygame.display.set_mode((595, 600))
background = pygame.image.load("a.png")

#
def draw(state, board, display):
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    board.draw_board(state, display)
    pygame.display.update()

def human_turn(state, board):
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.handle_click(pos, state)

def game(playerMode):
    state = State(9)
    board = View(9, state.board)
    draw(state, board, screen)
    while True:
        cur_turn = 0 if state.turn == 1 else 1
        match playerMode[cur_turn]:
            case PlayerMode.HUMAN:
                human_turn(state, board)
            case PlayerMode.AI_EASY:
                execute_minimax_move(board, state, min_num_enemy_moves, 3)
                time.sleep(1)
            case PlayerMode.AI_MEDIUM:
                execute_minimax_move(board, state, piece_enemy_moves, 3)
                time.sleep(1)
            case PlayerMode.AI_HARD:
                execute_minimax_move(board, state, move_dif_eval, 3)
                time.sleep(1)
        draw(state, board, screen)
        i = state.is_game_over()
        if i != 0:
            print("player " + str(i) + " won!")
            time.sleep(20000)
            break
        

gameMode = draw_main_menu()
print(gameMode)
game(gameMode)
