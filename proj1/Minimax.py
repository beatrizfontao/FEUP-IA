from State import *
from View import *
from copy import deepcopy
import math
import numpy as np

#State history used to avoid repeated states
history = []

"""
Minimax Algorithm with Alpha-Beta Cuts
Returns the best evaluation, the best move to make and the pice that should make that move
"""
def minimax(state, depth, alpha, beta, maximizing, evaluation_func):
    if depth == 0 or state.is_game_over():
        return evaluation_func(state), None, None
    
    if maximizing:
        max_eval = -math.inf
        best_piece = None
        best_move = None
        for piece, moves in state.get_valid_moves(state.turn):
            for move in moves:
                new_state = deepcopy(state)
                new_state.move(piece[0], piece[1], move[0], move[1])
                if matrix_in_list(new_state.board):
                    continue
                eval, _, _ = minimax(new_state, depth-1, alpha, beta, False, evaluation_func)
                if  eval > max_eval:
                    max_eval = eval
                    best_piece = piece
                    best_move = move
                alpha = max(eval, max_eval)
                if alpha >= beta:
                    break
        m_eval = max_eval
    else:
        min_eval = math.inf
        best_piece = None
        best_move = None
        for piece, moves in state.get_valid_moves(state.turn):
            for move in moves:
                new_state = deepcopy(state)
                new_state.move(piece[0], piece[1], move[0], move[1])
                if matrix_in_list(new_state.board):
                    continue
                eval, _, _ = minimax(new_state, depth-1, alpha, beta, True, evaluation_func)
                if eval < min_eval:
                    min_eval = eval
                    best_piece = piece
                    best_move = move
                beta = min(eval, min_eval)
                if alpha <= beta:
                    break
        m_eval = min_eval
    return m_eval, best_piece, best_move

"""
Evalution Function
Returns the negative total number of moves the player has
"""
def min_num_enemy_moves(state):
    available_moves = state.get_valid_moves(state.turn)
    num_moves = 0
    for _, moves in available_moves:
        n = len(moves)
        if n == 0:
            return math.inf
        num_moves += n

    return -num_moves

"""
Evaluation Function
Returns the negative number of moves that the piece with the least amount of moves of a player has
"""
def piece_enemy_moves(state):
    available_moves = state.get_valid_moves(state.turn)
    num_moves = math.inf
    for _, moves in available_moves:
        n = len(moves)
        if n == 0:
            return math.inf
        num_moves = min(num_moves, n)

    return -num_moves

"""
Evaluation Function
Similar to piece_enemy_moves, but subtracts the number of moves that the piece with the least amount of moves of the player with the value for the opponent 
"""
def move_dif_eval(state):
    player_moves = state.get_valid_moves(3 - state.turn)
    player_num_moves = 0
    for _, moves in player_moves:
        n = len(moves)
        if n == 0:
            return -math.inf
        player_num_moves = min(player_num_moves, n)
    opponent_moves = state.get_valid_moves(state.turn)
    opponent_num_moves = 0
    for _, moves in opponent_moves:
        n = len(moves)
        if n == 0:
            return math.inf
        opponent_num_moves = min(opponent_num_moves, n)
    return player_num_moves - opponent_num_moves

"""
Applies the minimax function to the given state with the evaluation function and executes the move.
Updates the history list with the new state.
"""
def execute_minimax_move(board, state, evaluation_func, depth):
    _, piece, move = minimax(state, depth, -math.inf, math.inf, True, evaluation_func)
    state.move(piece[0], piece[1], move[0], move[1])
    history.append(np.array(state.board))
    board.update(piece[0], piece[1], move[0], move[1])

"""
Checks the state already is in the state history
This avoids repeated states 
"""
def matrix_in_list(state):
    return any(np.array_equal(m, state) for m in history)