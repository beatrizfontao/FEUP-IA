import pygame, sys, time
from State import State
from View import View
from NewMinimax import *

from Menu import *

pygame.init()

#Screen and Background
screen = pygame.display.set_mode((595, 600))
background = pygame.image.load("images/a.png")

hint = pygame.image.load("images/hint.png")
width = hint.get_rect().width
height = hint.get_rect().height
hint = pygame.transform.scale(hint, (width/5, height/5))


"""
Draws the current state of the game on the screen
"""
def draw(state, board, display):
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    screen.blit(hint, (530,20))
    board.draw_board(state, display)
    pygame.display.update()

"""
Identifies when the human player clicks on the screen and processes those clicks inside the handle_click function
"""
def human_turn(state, board):
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.handle_click(pos, state)

"""
Game loop. Receives the game mode chosen by the user and contains a while true loop that breaks when either one of the players wins the game
"""
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
            time.sleep(5)
            break
        
#Invoke the menu drawing function and the game loop
gameMode = draw_main_menu()
game(gameMode)
