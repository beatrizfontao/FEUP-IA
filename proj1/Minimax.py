from copy import deepcopy
from Board import *
    
def execute_minimax_move(board, evaluate_func, depth):
    best_move = None
    best_eval = float('-inf')
    for (piece, moves) in board.get_valid_moves(board.turn):
            for move in moves:
                copy_board = deepcopy(board)
                copy_board.move(piece, move[0], move[1])
                new_state_eval = minimax(copy_board, depth - 1, float('-inf'), float('inf'), False, board.turn, evaluate_func)
            if new_state_eval > best_eval:
                best_move = (piece, move)
                best_eval = new_state_eval
    
    (piece, move) = best_move
    board.move(piece, move[0], move[1])

def minimax(state, depth, alpha, beta, maximizing, player, evaluate_func):
    if depth == 0 or state.is_game_over() != 0:
        return evaluate_func(state, player) * (1 if player == 'player1' else -1)
    
    if maximizing:
        max_eval = float('-inf')
        for (piece, moves) in state.get_valid_moves(state.turn):
            for move in moves:
                copy_state = deepcopy(state)
                copy_state.move(piece, move[0], move[1])
                eval = minimax(copy_state, depth - 1, alpha, beta, False, player, evaluate_func)
                alpha = max(max_eval, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for (piece, moves) in state.get_valid_moves(state.turn):
            for move in moves:
                copy_state = deepcopy(state)
                copy_state.move(piece, moves[0], move[1])
                eval = minimax(copy_state, depth - 1, alpha, beta, True, player, evaluate_func)
                beta = min(min_eval, eval)
                if alpha <= beta:
                    break
        return min_eval

def enemy_min_moves(board, player):
    min = float('inf')
    index = -1
    for i in range(len(board.pieces)):
        if board.pieces[i].player == player:
            min_moves = len(board.piece_valid_moves(board.pieces[i].row, board.pieces[i].col))
            if  min_moves < min:
                min = min_moves
                index = i
    return (index, min)