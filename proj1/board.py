from piece import *

class Board:
    #tamanho do tabuleiro deve ser impar
    def __init__(self, size, image):
        self.size = size
        self.image = image
        self.numPieces = (size - 1)*2
        start = size // 2

        #Create pieces
        self.pieces = []
        for i in range(start-1, start + 3, 2):
            for j in range(0, size):
                if j >= 0 and j < start:
                    piece = Piece(i, j, 'white')
                    self.pieces.append(piece)
                elif j >= start+1 and j < size:
                    piece = Piece(i, j, 'black')
                    self.pieces.append(piece)

    def print_pieces(self):
        for obj in self.pieces:
            print(obj.row)
            print(obj.col)
            print(obj.color)

#TEST
#b = Board(11)
#print(b.numPieces)
#b.print_pieces()
#b.pieces[0].move(1,1)
#print('-----------------------')
#b.print_pieces()
