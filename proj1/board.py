from piece import *

class Board:
    #Size must be odd
    def __init__(self, size):
        self.size = size
        self.numPieces = (size - 1)*2
        start = size // 2
        self.center = start - 1

        #Create pieces
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

    def is_cell_empty(self, row, col):
        for obj in self.pieces:
            if obj.row == row and obj.col == col:
                return False
        return True
    
    def is_cell_forbidden(self, row, col):
        for (r,c) in self.forbidden_cells:
            if r == row and c == col:
                return True
        return False
    
    def vertical_path_empty(self, col, init_row, new_row):
        #Down
        if init_row < new_row:
            start = init_row + 1
            end = new_row + 1
        #Up
        else:
            start = new_row
            end = init_row
        for i in range(start, end):
            if not self.is_cell_empty(i, col):
                print("up false")
                return False
        return True
            
    def horizontal_path_empty(self, row, init_col, new_col):
        #Right
        if init_col < new_col:
            start = init_col
            end = new_col
        #Left
        else:
            start = new_col
            end = init_col
        for i in range(start, end):
            if not self.is_cell_empty(row, i):
                print("Horizontal path not empty")
                return False  
        return True

    #TODO: add case for circular move
    def is_path_empty(self, init_row, init_col, new_row, new_col):
        #Horizontal move
        if init_row == new_row:
            if self.horizontal_path_empty(init_row, init_col, new_col):
                return True
        #Vertical move
        elif init_col == new_col:
            if self.vertical_path_empty(init_col, init_row, new_row):
                return True

        #Circular move
        #VERMELHO
        if init_row == new_col: 
            #meio de cima para esquerda
            if init_row < self.center:
                #ver se a horizontal e vertical estao vazias
                if self.horizontal_path_empty(init_row, init_col, self.center) and self.vertical_path_empty(new_col, self.center, new_row):
                    return True
            #meio de baixo para a direita   
            elif init_row > self.center + 2:
                if self.horizontal_path_empty(init_row, init_col, self.center+2) and self.vertical_path_empty(new_col, self.center+2, new_row):
                    return True
        #VERDE
        elif init_col == new_row:
            if init_col < self.center:
                if self.vertical_path_empty(init_col, init_row, self.center) and self.horizontal_path_empty(new_row, self.center, new_col):
                    return True
            #meio de baixo para a direita   
            elif init_col > self.center + 2:
                if self.vertical_path_empty(init_col, init_row, self.center+2) and self.horizontal_path_empty(new_row, self.center+2, new_col):
                    return True
        #AMARELO
        elif new_col == self.size - 1 - init_row:
            if self.horizontal_path_empty(init_row, init_col, self.center + 2) and self.vertical_path_empty(new_col, self.center, new_row):
                return True
        #ROXO
        elif new_row == self.size - 1 - init_col:
            if self.vertical_path_empty(init_col, init_row, self.center) and self.horizontal_path_empty(new_row, self.center+2, new_col):
                return True
        #ROSA
        elif new_col == self.size - 1 - init_row:
            if self.vertical_path_empty(init_col, init_row, self.center + 2) and self.horizontal_path_empty(new_row, self.center, new_col):
                return True
        #LARANJA
        elif new_row == self.size - 1 - init_col:
            if self.horizontal_path_empty(init_row, init_col, self.center) and self.vertical_path_empty(new_col, self.center + 2, new_row):
                return True
        return False
        
            

    #Checks if the move chosen is valid. Return True if it is and False otherwise
    def valid_move(self, piece, new_col, new_row):
        #check if the move is valid
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
    
    #Checks if the chosen move is valid and moves the piece. Returns true if the move is valid and false otherwise.
    def move_piece(self, init_row, init_col, color, new_row, new_col):
        can_play = False
        for piece in self.pieces:
            if piece.row == init_row and piece.col == init_col:
                #Check turn
                if piece.color == color:
                    can_play = True
                    p = piece
                else:
                    print("You can't move the other player's piece.")
                    return False
        if self.valid_move(p, new_col, new_row) and can_play:
            for obj in self.pieces:
                if obj.is_equal(p):
                    obj.move(new_col, new_row)
            return True
        else:
            print("Invalid move!aaaaa")
            return False

    def print_pieces(self):
        print("pieces: ")
        for obj in self.pieces:
            print(obj.row, obj.col)
            print(obj.color)
            print('')

#TEST
b = Board(9)
#print(b.numPieces)
#b.printPieces()
p = Piece(3,3,'black')
                       #col, row
b.move_piece(1, 3, 'white', 3, 1)
b.print_pieces()