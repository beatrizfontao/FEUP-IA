from Piece import *


class Board:
    # Size must be odd
    def __init__(self, size):
        self.size = size
        self.numPieces = (size - 1)*2
        start = size // 2
        self.center = start - 1

        # Create pieces
        self.pieces = []
        for i in range(start-1, start + 3, 2):
            for j in range(size):
                if j >= 0 and j < start:
                    piece = Piece(i, j, 'player1')
                    self.pieces.append(piece)
                elif j >= start+1 and j < size:
                    piece = Piece(i, j, 'player2')
                    self.pieces.append(piece)

        self.forbidden_cells = []
        for i in range(size):
            for j in range(size):
                if (i >= 0 and i < start - 1) or (i > start + 1 and i < size):
                    if (j >= 0 and j < start - 1) or (j > start + 1 and j < size):
                        cell = (i, j)
                        self.forbidden_cells.append(cell)

        self.circle_paths = []
        for num in range(self.center):
            circle = []
            # top
            for col in range(num, size - num - 1):
                pos = (num, col)
                if pos not in self.forbidden_cells:
                    circle.append(pos)
            # right
            col = size - 1 - num
            for row in range(num, size - num):
                pos = (row, col)
                if pos not in self.forbidden_cells:
                    circle.append(pos)
            # bottom
            row = size - 1 - num
            for col in reversed(range(num, size - num - 1)):
                pos = (row, col)
                if pos not in self.forbidden_cells:
                    circle.append(pos)
            # left
            for row in reversed(range(num, size - num - 1)):
                pos = (row, num)
                if pos not in self.forbidden_cells:
                    circle.append(pos)
            self.circle_paths.append(circle)

    def is_cell_empty(self, row, col):
        for obj in self.pieces:
            if obj.row == row and obj.col == col:
                return False
        return True

    def vertical_valid_moves(self, row, col):
        valid_moves = []
        cur_row = (row + 1) % self.size
        while cur_row != row:
            if not self.is_cell_empty(cur_row, col):
                break
            else:
                valid_moves.append((cur_row, col))
            cur_row = (cur_row + 1) % self.size

        cur_row = (row - 1) % self.size
        while cur_row != row:
            if not self.is_cell_empty(cur_row, col):
                break
            else:
                valid_moves.append((cur_row, col))
            cur_row = (cur_row - 1) % self.size
        return valid_moves

    def horizontal_valid_moves(self, row, col):
        valid_moves = []
        cur_col = (col + 1) % self.size
        while cur_col != col:
            if not self.is_cell_empty(row, cur_col):
                break
            else:
                valid_moves.append((row, cur_col))
            cur_col = (cur_col + 1) % self.size

        cur_col = (col - 1) % self.size
        while cur_col != col:
            if not self.is_cell_empty(row, cur_col):
                break
            else:
                valid_moves.append((row, cur_col))
            cur_col = (cur_col - 1) % self.size
        return valid_moves

    def find_circular_path(self, row, col):
        if 0 <= row < self.center and self.center <= col < self.center + 3:
            return row
        elif self.center <= row < self.center + 3 and 0 < col < self.center:
            return col
        elif self.center + 2 < row < self.size and self.center <= col < self.center + 3:
            return self.size - 1 - row
        elif self.center <= row < self.center + 3 and self.center + 2 < col < self.size:
            return self.size - 1 - col
        else:
            return -1

    def get_index(self, element, list):
        for i in range(len(list)):
            if list[i] == element:
                return i
        return -1

    def circular_valid_moves(self, row, col):
        valid_moves = []

        c = self.find_circular_path(row, col)
        if c == -1:
            return []

        i = self.get_index((row, col), self.circle_paths[c])
        l = len(self.circle_paths[c])
        j = (i+1) % l
        cur_pos = self.circle_paths[c][j]

        while cur_pos != (row, col):
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            else:
                valid_moves.append((cur_pos[0], cur_pos[1]))
            j = (j + 1) % l
            cur_pos = self.circle_paths[c][j]

        j = (i-1) % l
        cur_pos = self.circle_paths[c][j]

        while cur_pos != (row, col):
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            else:
                valid_moves.append((cur_pos[0], cur_pos[1]))
            j = (j - 1) % l
            cur_pos = self.circle_paths[c][j]
        return valid_moves

    # Checks if the chosen move is valid and moves the piece. Returns true if the move is valid and false otherwise.
    def move_piece(self, init_row, init_col, player, new_row, new_col):
        right_turn = False
        for piece in self.pieces:
            if piece.row == init_row and piece.col == init_col:
                # Check turn
                if piece.player == player:
                    right_turn = True
                    p = piece
                else:
                    print("You can't move the other player's piece.")
                    return False
        valid_moves = self.piece_valid_moves(init_row, init_col)
        if right_turn and (new_row, new_col) in valid_moves:
            for obj in self.pieces:
                if obj.is_equal(p):
                    obj.move(new_col, new_row)
            return True
        else:
            return False

    def piece_valid_moves(self, row, col):
        return [*set(self.horizontal_valid_moves(row, col) + self.vertical_valid_moves(row, col) + self.circular_valid_moves(row, col))]
    
    def is_game_over(self):
        for piece in self.pieces:
            valid_moves = self.piece_valid_moves(piece.row, piece.col)
            if len(valid_moves) == 0:
                return 1 if piece.player == 'player2' else 2
        return 0

    def print_pieces(self):
        print("pieces: ")
        for obj in self.pieces:
            print(obj.row, obj.col)
            print(obj.player)
            print('')