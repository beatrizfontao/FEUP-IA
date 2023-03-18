from Board import *

def greedy_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    setattr(NPuzzleState, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set() # to not visit the same state twice
    
    while states:
        current = heapq.heappop(states)
        visited.add(current)

        if current.is_complete():
            return current.move_history
    
        for child in current.children():
            if child not in visited:
                heapq.heappush(states, child)

def a_star_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer

    # this is very similar to greedy, the difference is that it takes into account the cost of the path so far
    return greedy_search(problem, lambda state: heuristic(state) + len(state.move_history) - 1)

def enemy_min_moves(board, player):
    min = sys.maxsize
    min_piece = None
    for piece in board.pieces:
        if piece.player == player:
            min_moves = len(board.piece_valid_moves(piece.row, piece.col))
            if  min_moves < min:
                min = min_moves
                min_piece = piece 
    return min_piece