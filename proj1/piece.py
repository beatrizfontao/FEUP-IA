class Piece:
    def __init__(self, col, row, player):
        self.col = col
        self.row = row
        self.player = player
    
    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow

    def is_equal(self, piece):
        return self.row == piece.row and self.col == piece.col and self.player == piece.player