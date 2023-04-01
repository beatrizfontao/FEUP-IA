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

        print(self.circle_paths)

    def move(self, col, row, new_col, new_row):
        player = self.board[row][col]
        self.board[row][col] = 0
        self.board[new_row][new_col] = player
        self.turn = 3 - self.turn

    def is_game_over(self):
        print('aa')
        print(self.board)
        pieces = self.get_player_pieces(1) + self.get_player_pieces(2)
        for piece in pieces:
            valid_moves = self.piece_valid_moves(piece[1], piece[0])
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
            for col in range(len(self.board[row])):
                if self.board[row][col] == player:
                    moves.append(((col, row), self.piece_valid_moves(col, row)))
        return moves

    def is_cell_empty(self, col, row):
        return True if self.board[row][col] == 0 else False

    def vertical_valid_moves(self, col, row):
        valid_moves = []

        cur_row = (row + 1) % self.size
        while cur_row != row:
            if not self.is_cell_empty(col, cur_row):
                break
            if self.board[cur_row][col] == -1:
                break
            else:
                valid_moves.append((col, cur_row))
            cur_row = (cur_row + 1) % self.size

        cur_row = (row - 1) % self.size
        while cur_row != row:
            if not self.is_cell_empty(col, cur_row):
                break
            if self.board[cur_row][col] == -1:
                break
            else:
                valid_moves.append((col, cur_row))
            cur_row = (cur_row - 1) % self.size
        
        return valid_moves

    def horizontal_valid_moves(self, col, row):
        valid_moves = []
        cur_col = (col + 1) % self.size
        while cur_col != col:
            if not self.is_cell_empty(cur_col, row):
                break
            if self.board[row][cur_col] == -1:
                break
            else:
                valid_moves.append((cur_col, row))
            cur_col = (cur_col + 1) % self.size

        cur_col = (col - 1) % self.size
        while cur_col != col:
            if not self.is_cell_empty(cur_col, row):
                break
            if self.board[row][cur_col] == -1:
                break
            else:
                valid_moves.append((cur_col, row))
            cur_col = (cur_col - 1) % self.size

        return valid_moves

    def find_circular_path(self, col, row):
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

    def circular_valid_moves(self, col, row):
        valid_moves = []

        c = self.find_circular_path(col, row)
        if c == -1:
            return []
        
        i = self.get_index((col,row), self.circle_paths[c])
        l = len(self.circle_paths[c])
        j = (i+1) % l
        cur_pos = self.circle_paths[c][j]

        while cur_pos != (row, col):
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            else:
                valid_moves.append(cur_pos)
            j = (i-1) % l
            cur_pos = self.circle_paths[c][j]

        j = (i-1) % l
        cur_pos = self.circle_paths[c][j]

        while cur_pos != (col, row):
            if not self.is_cell_empty(cur_pos[0], cur_pos[1]):
                break
            else:
                valid_moves.append(cur_pos)
            j = (j - 1) % l
            cur_pos = self.circle_paths[c][j]

        return valid_moves

    def piece_valid_moves(self, col, row):
        return [*set(self.horizontal_valid_moves(col, row) + self.vertical_valid_moves(col, row) + self.circular_valid_moves(col, row))]

    def handle_player_move(self, clicked_col, clicked_row, piece_col, piece_row):
        if (clicked_col, clicked_row) in self.piece_valid_moves(piece_col, piece_row):
            self.move(piece_col, piece_row, clicked_col, clicked_row)
            return True
        return False
    
s = State(9)
s.piece_valid_moves(3,1)