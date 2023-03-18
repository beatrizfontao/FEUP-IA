from enum import Enum
from Board import *

class PlayerMode(Enum):
    HUMAN = 1
    AI_HARD = 2
    AI_MEDIUM = 3
    AI_EASY = 4

def ask_move(player_turn):
    print(player_turn + ' turn')
    init_row = int(input('Initial Row: '))
    init_col = int(input('Initial Col: '))
    new_row = int(input('New Row: '))
    new_col = int(input('New Col: '))
    return [(init_row, init_col), (new_row, new_col)]

def game(size, mode):
    board = Board(size)
    player_turn = 'player1'
    game_over = 0
    while game_over == 0:
        valid_move = False
        while not valid_move:
            move = ask_move(player_turn)
            valid_move = board.move_piece(move[0][0], move[0][1], player_turn, move[1][0], move[1][1])
        player_turn = 'player1' if player_turn == 'player2' else 'player2'
        game_over = board.is_game_over()
    if game_over == 1:
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

if __name__ == "__main__":
    game(9, 1)
