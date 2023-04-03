from State import *
from View import *
from copy import deepcopy
import math
import numpy as np

history = []

def max_value(state, depth, alpha, beta, evaluate):
    if depth == 0 or state.is_game_over():
        return evaluate(state), None, None
    
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
    return value, best_piece, best_move

def min_value(state, depth, alpha, beta, evaluate):
    if depth == 0 or state.is_game_over():
        return evaluate(state), None, None
    
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

def minimax(state, depth, alpha, beta, maximizing_player, evaluate):
    if maximizing_player:
        value, piece, move = max_value(state, depth, alpha, beta, evaluate)
    else:
        value, piece, move = min_value(state, depth, alpha, beta, evaluate)
    return value, piece, move


def move_dif_eval(state):
    player_moves = state.get_valid_moves(state.turn)
    player_num_moves = 0
    for piece, moves in player_moves:
        n = len(moves)
        if n == 0:
            return math.inf
        player_num_moves += n
    opponent_moves = state.get_valid_moves(3 - state.turn)
    opponent_num_moves = 0
    for piece, moves in opponent_moves:
        n = len(moves)
        if n == 0:
            return -math.inf
        opponent_num_moves += n
    return player_num_moves - opponent_num_moves

def piece_enemy_moves(state):
    available_moves = state.get_valid_moves(3 - state.turn)
    num_moves = math.inf
    for piece, moves in available_moves:
        n = len(moves)
        num_moves = min(num_moves, n)

    return -num_moves

def execute_minimax_move(board, state, evaluate_func, depth):
    _, piece, move = minimax(state, depth, -math.inf, math.inf, True, evaluate_func)
    state.move(piece[0], piece[1], move[0], move[1])
    history.append(np.array(state.board))
    board.update(piece[0], piece[1], move[0], move[1])

def matrix_in_list(state):
    return any(np.array_equal(m, state) for m in history)