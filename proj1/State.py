import numpy as np

"""
State Representation. This class leads with the game representation and logic
Board is a matrix where -1 is a forbidden cell (i.e. not a part of the board), 0 is an empty cell, 1 is a piece of the player 1 and 2 is a piece of the player 2
"""
class State:
   
    def __init__(self, size):
        self.size = size #size of the board
        start = size // 2 #
        self.center = start - 1 #index of the beginning of the center square of the board
        self.turn = 1 #player turn

        #Initializing the board with all zeros and puts the pieces in the starting positions
        self.board = np.zeros((size,size))
        
        for i in range(size):
            for j in range(size):
                if (i >= 0 and i < start - 1) or (i > start + 1 and i < size):
                    if (j >= 0 and j < start - 1) or (j > start + 1 and j < size):
                        self.board[i][j] = -1

        for i in range(start-1, start + 3, 2):
            for j in range(size):
                if j >= 0 and j < start:
                    self.board[i][j] = 1
                elif j >= start+1 and j < size:
                    self.board[i][j] = 2

        #Initializes the circle_paths, which are the paths a piece can take around the board
        self.circle_paths = []
        for num in range(self.center):
            circle = []
            # top
            for col in range(num, size - num - 1):
                pos = (num, col)
                if self.board[num][col] != -1:
                    circle.append(pos)
            # right
            col = size - 1 - num
            for row in range(num, size - num):
                pos = (row, col)
                if self.board[row][col] != -1:
                    circle.append(pos)
            #bottom
            row = size - 1 - num
            for col in reversed(range(num, size - num - 1)):
                pos = (row, col)
                if self.board[row][col] != -1:
                    circle.append(pos)
            # left
            for row in reversed(range(num, size - num - 1)):
                pos = (row, num)
                if self.board[row][num] != -1:
                    circle.append(pos)
            self.circle_paths.append(circle)

    """
    Moves the piece in the position (row, col) to the position (new_row, new_col)
    """
    def move(self, row, col, new_row, new_col):
        player = self.board[row][col]
        self.board[row][col] = 0
        self.board[new_row][new_col] = player
        self.turn = 3 - self.turn

    """
    Checks if the game is over
    Returns the number of the player that won or 0 if no one won wet
    """
    def is_game_over(self):
        pieces = self.get_player_pieces(1) + self.get_player_pieces(2)
        for piece in pieces:
            valid_moves = self.piece_valid_moves(piece[0], piece[1])
            if len(valid_moves) == 0:
                return 1 if self.board[piece[0]][piece[1]] == 2 else 2
        return 0
    
    """
    Returns a list with the positions (row,col) of the pieces of a player
    """
    def get_player_pieces(self, player):
        pieces = []
        for i in range(self.size):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    pieces.append((i, j))
        return pieces
    
    """
    Returns a list of tuples with the pieces if the player and the respective moves those pieces can make
    """
    def get_valid_moves(self, player):
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == player:
                    moves.append(((row, col), self.piece_valid_moves(row, col)))
        return moves

    """
    Checks if the cell (row, col) of the board is empty
    Returns True if the cell is empty or False otherwise
    """
    def is_cell_empty(self, row, col):
        return True if self.board[row][col] == 0 else False

    """
    Returns the vertical moves of a piece in position (row,col). 
    Since a piece can move from up to down and down to up, it must check both ways
    """
    def vertical_valid_moves(self, row, col):
        valid_moves = []
        
        #Checks from up to down a column
        cur_row = (row + 1) % self.size
        while cur_row != row:
            #If the cell isn't empty, the piece can't move there
            if not self.is_cell_empty(cur_row, col):
                break
            #If it enters a cell out of bounds, the piece can't move
            if self.board[cur_row][col] == -1:
                break
            #Otherwise the piece can freely move to that position
            else:
                valid_moves.append((cur_row, col))
            cur_row = (cur_row + 1) % self.size

        #Checks from down to up a column
        cur_row = (row - 1) % self.size
        while cur_row != row:
            #If the cell isn't empty, the piece can't move there
            if not self.is_cell_empty(cur_row, col):
                break
            #If it enters a cell out of bounds, the piece can't move
            if self.board[cur_row][col] == -1:
                break
            #Otherwise the piece can freely move to that position
            else:
                valid_moves.append((cur_row, col))
            cur_row = (cur_row - 1) % self.size
        
        return valid_moves

    """
    Returns the horizontal moves of a piece in position (row,col). 
    Since a piece can move from left to right and right to left, it must check both ways
    """
    def horizontal_valid_moves(self, row ,col):
        valid_moves = []

        #Checks from left to right a row
        cur_col = (col + 1) % self.size
        while cur_col != col:
            #If the cell isn't empty, the piece can't move there
            if not self.is_cell_empty(row, cur_col):
                break
            #If it enters a cell out of bounds, the piece can't move
            if self.board[row][cur_col] == -1:
                break
            #Otherwise the piece can freely move to that position
            else:
                valid_moves.append((row, cur_col))
            cur_col = (cur_col + 1) % self.size

        #Checks from right to left a row
        cur_col = (col - 1) % self.size
        while cur_col != col:
            #If the cell isn't empty, the piece can't move there
            if not self.is_cell_empty(row, cur_col):
                break
            #If it enters a cell out of bounds, the piece can't move
            if self.board[row][cur_col] == -1:
                break
            #Otherwise the piece can freely move to that position
            else:
                valid_moves.append((row, cur_col))
            cur_col = (cur_col - 1) % self.size

        return valid_moves

    """
    Returns the circular valid moves of a piece in position (row, col). 
    Since a piece can move from clockwise or counter clockwise, it must check both ways
    """
    def circular_valid_moves(self, row, col):
        valid_moves = []

        #Checks if there is a valid circular path. The piece must be in a position that allows circular moves
        c = self.find_circular_path(row, col)
        if c == -1:
            return []
        
        i = self.get_index((row, col), self.circle_paths[c])
        l = len(self.circle_paths[c])
        j = (i+1) % l
        cur_pos = self.circle_paths[c][j]

        #Checks clockwise path
        while cur_pos != (row, col):
            #If the cell isn't empty, the piece can't move there
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            #Otherwise the piece can freely move to that position
            else:
                valid_moves.append(cur_pos)
            j = (j + 1) % l
            cur_pos = self.circle_paths[c][j]

        j = (i-1) % l
        cur_pos = self.circle_paths[c][j]

        #Checks counter clockwise path
        while cur_pos != (row, col):
            #If the cell isn't empty, the piece can't move there
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            #Otherwise the piece can freely move to that position
            else:
                valid_moves.append(cur_pos)
            j = (j - 1) % l
            cur_pos = self.circle_paths[c][j]

        return valid_moves

    """
    Checks if a piece is in a valid circular path and returns the index of that circular path in the array
    If it isn't in a position that allows circular moves, returns -1
    """
    def find_circular_path(self, row, col):
        if 0 <= row < self.center and self.center <= col < self.center + 3:
            return row
        elif self.center <= row < self.center + 3 and 0 <= col < self.center:
            return col
        elif self.center + 2 < row < self.size and self.center <= col < self.center + 3:
            return self.size - 1 - row
        elif self.center <= row < self.center + 3 and self.center + 2 < col < self.size:
            return self.size - 1 - col
        else:
            return -1
    
    """
    Returns the index of an element that belongs to a list
    If the element doesn't belong to the list, returns -1
    """
    def get_index(self, element, list):
        for i in range(len(list)):
            if list[i] == element:
                return i
        return -1

    """
    Returns a list with all the valid moves a the piece in the position (row, col) has
    This includes all its horizontal, vertical and circular moves 
    """
    def piece_valid_moves(self, row, col):
        return [*set(self.horizontal_valid_moves(row, col) + self.vertical_valid_moves(row, col) + self.circular_valid_moves(row, col))]

    """
    Receives a position of a piece (piece_col, piece_row) and a desired new position for that piece (clicked_col, clicked_row).
    Returns True if the move is valid or False otherwise
    """
    def handle_player_move(self, clicked_col, clicked_row, piece_col, piece_row):
        if (clicked_col, clicked_row) in self.piece_valid_moves(piece_col, piece_row):
            self.move(piece_col, piece_row, clicked_col, clicked_row)
            return True
        return False
