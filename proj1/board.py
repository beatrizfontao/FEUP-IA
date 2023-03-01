import piece

class Board:
    #tamanho do tabuleiro deve ser impar
    def __init__(self, size):
        self.size = size
        self.numPieces = size - 3
        start = size // 2

        #Create pieces
        self.pieces = []
        for i in range(start, start + 3, 2):
            for j in range(0, size):
                if j >= 0 and j < start:
                    piece = Piece(i, j, 'white')
                    self.pieces.append(piece)
                elif j >= start+3 and j < size:
                    piece = Piece(i, j, 'black')
                    self.pieces.append(piece)
