from State import *
from View import *
from copy import deepcopy
    
def execute_minimax_move(board, state, evaluate_func, depth):
    best_move = None
    best_eval = float('-inf')
    for (piece, moves) in state.get_valid_moves(state.turn):
        for move in moves:
            if(piece == (3,1) and move == (4,1)):
                print("a")
            copy_state = deepcopy(state)
            copy_state.move(piece[0], piece[1], move[0], move[1])
            new_state_eval = minimax(copy_state, depth - 1, float('-inf'), float('inf'), False, state.turn, evaluate_func)
            print(state.turn, new_state_eval, piece, move)
            if new_state_eval > best_eval:
                best_move = (piece, move)
                best_eval = new_state_eval
    
    print(best_move)
    (piece, move) = best_move
    state.move(piece[0], piece[1], move[0], move[1])
    board.update(piece[0], piece[1], move[0], move[1])

def minimax(state, depth, alpha, beta, maximizing, player, evaluate_func):
    if depth == 0 or state.is_game_over() != 0:
        return evaluate_func(state) #* (1 if player == 1 else -1)
    
    if maximizing:
        max_eval = float('-inf')
        for (piece, moves) in state.get_valid_moves(state.turn):
            for move in moves:
                copy_state = deepcopy(state)
                copy_state.move(piece[0], piece[1], move[0], move[1])
                eval = minimax(copy_state, depth - 1, alpha, beta, False, player, evaluate_func)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for (piece, moves) in state.get_valid_moves(state.turn):
            for move in moves:
                copy_state = deepcopy(state)
                copy_state.move(piece[0], piece[1], move[0], move[1])
                eval = minimax(copy_state, depth - 1, alpha, beta, True, player, evaluate_func)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha <= beta:
                    break
        return min_eval

<<<<<<< HEAD
def num_enemy_moves(state):
    available_moves = len(state.get_valid_moves(state.turn))
    return float('-inf') if available_moves == 0 else available_moves
=======
def min_num_enemy_moves(state):
    available_moves = state.get_valid_moves(3 - state.turn)
    num_moves = 0
    for piece, moves in available_moves:
        n = len(moves)
        num_moves += n

    return num_moves
    
def min_piece_enemy_moves(state):
    available_moves = state.get_valid_moves(3 - state.turn)
    num_moves = float('inf')
    for piece, moves in available_moves:
        n = len(moves)
        num_moves = min(num_moves, n)

    return num_moves

def dif_moves(state):
    available_moves_enemy = state.get_valid_moves(3 - state.turn)
    available_moves_cur = state.get_valid_moves(state.turn)
    num_moves_enemy = float('inf')
    for piece, moves in available_moves_enemy:
        n = len(moves)
        num_moves_enemy = min(num_moves_enemy, n)

    num_moves_cur = float('inf')
    for piece, moves in available_moves_cur:
        n = len(moves)
        num_moves_cur = min(num_moves_cur, n)
    return num_moves_enemy-num_moves_cur
>>>>>>> 216d9722141358e9b59ce34212ff6ee215790836
