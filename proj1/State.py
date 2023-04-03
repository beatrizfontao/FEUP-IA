import numpy as np

class State:
    # Size must be odd
    def __init__(self, size):
        self.size = size
        start = size // 2
        self.center = start - 1
        self.turn = 1

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


    def move(self, row, col, new_row, new_col):
        player = self.board[row][col]
        self.board[row][col] = 0
        self.board[new_row][new_col] = player
        self.turn = 3 - self.turn

    def is_game_over(self):
        pieces = self.get_player_pieces(1) + self.get_player_pieces(2)
        for piece in pieces:
            valid_moves = self.piece_valid_moves(piece[0], piece[1])
            if len(valid_moves) == 0:
                return 1 if self.board[piece[0]][piece[1]] == 2 else 2
        return 0
    
    def get_player_pieces(self, player):
        pieces = []
        for i in range(self.size):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    pieces.append((i, j))
        return pieces
    
    def get_valid_moves(self, player):
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == player:
                    moves.append(((row, col), self.piece_valid_moves(row, col)))
        return moves

    def is_cell_empty(self, row, col):
        return True if self.board[row][col] == 0 else False

    def vertical_valid_moves(self, row, col):
        valid_moves = []

        cur_row = (row + 1) % self.size
        while cur_row != row:
            if not self.is_cell_empty(cur_row, col):
                break
            if self.board[cur_row][col] == -1:
                break
            else:
                valid_moves.append((cur_row, col))
            cur_row = (cur_row + 1) % self.size

        cur_row = (row - 1) % self.size
        while cur_row != row:
            if not self.is_cell_empty(cur_row, col):
                break
            if self.board[cur_row][col] == -1:
                break
            else:
                valid_moves.append((cur_row, col))
            cur_row = (cur_row - 1) % self.size
        
        return valid_moves

    def horizontal_valid_moves(self, row ,col):
        valid_moves = []
        cur_col = (col + 1) % self.size
        while cur_col != col:
            if not self.is_cell_empty(row, cur_col):
                break
            if self.board[row][cur_col] == -1:
                break
            else:
                valid_moves.append((row, cur_col))
            cur_col = (cur_col + 1) % self.size

        cur_col = (col - 1) % self.size
        while cur_col != col:
            if not self.is_cell_empty(row, cur_col):
                break
            if self.board[row][cur_col] == -1:
                break
            else:
                valid_moves.append((row, cur_col))
            cur_col = (cur_col - 1) % self.size

        return valid_moves

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
                valid_moves.append(cur_pos)
            j = (j + 1) % l
            cur_pos = self.circle_paths[c][j]

        j = (i-1) % l
        cur_pos = self.circle_paths[c][j]

        while cur_pos != (row, col):
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            else:
                valid_moves.append(cur_pos)
            j = (j - 1) % l
            cur_pos = self.circle_paths[c][j]

        return valid_moves

    def piece_valid_moves(self, row, col):
        return [*set(self.horizontal_valid_moves(row, col) + self.vertical_valid_moves(row, col) + self.circular_valid_moves(row, col))]

    def handle_player_move(self, clicked_col, clicked_row, piece_col, piece_row):
        if (clicked_col, clicked_row) in self.piece_valid_moves(piece_col, piece_row):
            self.move(piece_col, piece_row, clicked_col, clicked_row)
            return True
        return False
