from State import *
from View import *
from copy import deepcopy
import math
import numpy as np

#State history used to avoid repeated states
history = []

def minimax(state, depth, alpha, beta, maximizing_player, evaluate):
    if depth == 0 or state.is_game_over():
        return evaluate(state), None, None
    
    if maximizing_player:
        value = -math.inf
        best_piece = None
        best_move = None
        for piece, moves in state.get_valid_moves(state.turn):
            for move in moves:
                new_state = deepcopy(state)
                new_state.move(piece[0], piece[1], move[0], move[1])
                if matrix_in_list(new_state.board):
                    continue
                new_value, _, _ = minimax(new_state, depth-1, alpha, beta, False, evaluate)
                if new_value > value:
                    value = new_value
                    best_piece = piece
                    best_move = move
                alpha = max(alpha, value)
                if alpha >= beta:
                    return value, best_piece, best_move
    else:
        value = math.inf
        best_piece = None
        best_move = None
        for piece, moves in state.get_valid_moves(state.turn):
            for move in moves:
                new_state = deepcopy(state)
                new_state.move(piece[0], piece[1], move[0], move[1])
                if matrix_in_list(new_state.board):
                    continue
                new_value, _, _ = minimax(new_state, depth-1, alpha, beta, True, evaluate)
                if new_value < value:
                    value = new_value
                    best_piece = piece
                    best_move = move
                beta = min(beta, value)
                if alpha <= beta:
                    return value, best_piece, best_move
    return value, best_piece, best_move

"""
Evaluation Function
"""
def move_dif_eval(state):
    player_moves = state.get_valid_moves(state.turn)
    player_num_moves = 0
    for _, moves in player_moves:
        n = len(moves)
        if n == 0:
            return math.inf
        player_num_moves += n
    opponent_moves = state.get_valid_moves(3 - state.turn)
    opponent_num_moves = 0
    for _, moves in opponent_moves:
        n = len(moves)
        if n == 0:
            return -math.inf
        opponent_num_moves += n
    return player_num_moves - opponent_num_moves

"""
Evaluation Function
"""
def piece_enemy_moves(state):
    available_moves = state.get_valid_moves(3 - state.turn)
    num_moves = math.inf
    for _, moves in available_moves:
        n = len(moves)
        num_moves = min(num_moves, n)

    return -num_moves

"""
Applies the minimax function to the given state with the evaluation function and executes the move.
Updates the history list with the new state.
"""
def execute_minimax_move(board, state, evaluate_func, depth):
    _, piece, move = minimax(state, depth, -math.inf, math.inf, True, evaluate_func)
    state.move(piece[0], piece[1], move[0], move[1])
    history.append(np.array(state.board))
    board.update(piece[0], piece[1], move[0], move[1])

"""
Checks the state already is in the state history
This avoids repeated states 
"""
def matrix_in_list(state):
    return any(np.array_equal(m, state) for m in history)