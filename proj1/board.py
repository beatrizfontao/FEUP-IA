from piece import *


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
                    piece = Piece(i, j, 'white')
                    self.pieces.append(piece)
                elif j >= start+1 and j < size:
                    piece = Piece(i, j, 'black')
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

    def is_cell_forbidden(self, row, col):
        for (r, c) in self.forbidden_cells:
            if r == row and c == col:
                return True
        return False

    def vertical_path_empty(self, col, init_row, new_row):
        cur_row = init_row
        while cur_row != new_row:
            cur_row = (cur_row + 1) % self.size
            if not self.is_cell_empty(cur_row, col):
                break
            if cur_row == new_row:
                return True
        cur_row = init_row
        while cur_row != new_row:
            cur_row = (cur_row - 1) % self.size
            if not self.is_cell_empty(cur_row, col):
                return False
            if cur_row == new_row:
                return True
        return False

    def horizontal_path_empty(self, row, init_col, new_col):
        cur_col = init_col
        while cur_col != new_col:
            cur_col = (cur_col + 1) % self.size
            if not self.is_cell_empty(row, cur_col):
                break
            if cur_col == new_col:
                return True
        cur_col = init_col
        while cur_col != new_col:
            cur_col = (cur_col - 1) % self.size
            if not self.is_cell_empty(row, cur_col):
                return False
            if cur_col == new_col:
                return True
        return False

    def find_circular_path(self, row, col):
        print('center = ', self.center)
        print('row = ', row)
        print('col = ', col)
        if 0 <= row < self.center and self.center <= col < self.center + 3:
            print('entrou')
            return row
        elif self.center <= row < self.center + 3 and 0 < col < self.center:
            return col
        elif self.center + 2 < row < self.size and self.center <= col < self.center + 3:
            return self.size - 1 - row
        elif self.center <= row < self.center + 3 and self.center + 2 < col < self.size:
            return self.size - 1 - col
        else:
            print('Invalid move')
            return -1

    def get_index(self, element, list):
        for i in range(len(list)):
            if list[i] == element:
                return i
        return -1

    def circular_path_empty(self, init_row, init_col, new_row, new_col):
        c = self.find_circular_path(init_row, init_col)
        print('c = ', c)
        if c == -1:
            return False

        i = self.get_index((init_row, init_col), self.circle_paths[c])
        print('index = ', i)
        l = len(self.circle_paths[c])
        cur_pos = (init_row, init_col)
        j = i
        while cur_pos != (new_row, new_col):
            j = (j + 1) % l
            cur_pos = self.circle_paths[c][j]
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            if cur_pos == (new_row, new_col):
                return True
        while cur_pos != (new_row, new_col):
            i = (i - 1) % l
            cur_pos = self.circle_paths[c][i]
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                return False
            if cur_pos == (new_row, new_col):
                return True

    # TODO: add case for circular move
    def is_path_empty(self, init_row, init_col, new_row, new_col):
        # Horizontal move
        if init_row == new_row:
            print("Same Row")
            if self.horizontal_path_empty(init_row, init_col, new_col):
                return True
        # Vertical move
        elif init_col == new_col:
            print("Same Col")
            if self.vertical_path_empty(init_col, init_row, new_row):
                return True
        # Circular move
        else:
            return self.circular_path_empty(init_row, init_col, new_row, new_col)

    # Checks if the move chosen is valid. Return True if it is and False otherwise
    def valid_move(self, piece, new_col, new_row):
        # check if the move is valid
        if piece.col == new_col and piece.row == new_row:
            print("Invalid move - same pos")
            return False
        elif self.is_cell_forbidden(new_row, new_col):
            print("Invalid move - forbidden move")
            return False
        else:
            if self.is_path_empty(piece.row, piece.col, new_row, new_col):
                print("Valid move")
                return True
            else:
                return False

    # Checks if the chosen move is valid and moves the piece. Returns true if the move is valid and false otherwise.
    def move_piece(self, init_row, init_col, color, new_row, new_col):
        can_play = False
        for piece in self.pieces:
            if piece.row == init_row and piece.col == init_col:
                # Check turn
                if piece.color == color:
                    can_play = True
                    p = piece
                else:
                    print("You can't move the other player's piece.")
                    return False
        print(can_play)
        if can_play and self.valid_move(p, new_col, new_row):
            for obj in self.pieces:
                if obj.is_equal(p):
                    obj.move(new_col, new_row)
            return True
        else:
            return False


    def piece_valid_moves(self, row, col):
        valid_moves = []
        cur_row = row
        cur_col = col
        # vertical
        a = True
        # down
        while a:
            cur_row = (cur_row + 1) % self.size
            a = self.vertical_path_empty(col, row, cur_row)
            if a:
                valid_moves.append((cur_row, col))
            else:
                break
        # up
        a = True
        cur_col = col
        while a:
            cur_col = (cur_col - 1) % self.size
            a = self.vertical_path_empty(col, cur_row, row)
            if a:
                valid_moves.append((cur_row, col))
            else:
                break
        #horizontal
                a = True
        # down
        while a:
            cur_row = (cur_row + 1) % self.size
            a = self.vertical_path_empty(col, row, cur_row)
            if a:
                valid_moves.append((cur_row, col))
            else:
                break
        # up
        a = True
        cur_row = row
        while a:
            cur_row = (cur_row - 1) % self.size
            a = self.vertical_path_empty(col, cur_row, row)
            if a:
                valid_moves.append((cur_row, col))
            else:
                break

    def print_pieces(self):
        print("pieces: ")
        for obj in self.pieces:
             print(obj.row, obj.col)
             print(obj.color)
             print('')
        # for a in self.circle_paths:
        #     print('--------')
        #     for (r, c) in a:
        #         print(r, c)

    # def has_available_moves(self, row, col, color):
    #     if row == 0 and self.center <= col < self.center + 3:
    #         self.is_cell_empty()

    #def game_over(self):


#TEST
b = Board(9)

#teste da a volta:
# b.move_piece(5, 3, 'black', 4, 3)
# b.move_piece(3, 5, 'white', 4, 5)
# b.print_pieces()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
# print('---')
# b.move_piece(4, 5, 'white', 4, 1)

#teste circulo
#1
#b.move_piece(1, 3, 'white', 3, 1)
#b.print_pieces()  
#a = b.circular_path_empty(1, 3, 3, 1)
#print(a) 