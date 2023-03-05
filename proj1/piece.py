class Piece:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
    
    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow

    def is_equal(self, piece):
        return self.row == piece.row and self.col == piece.col and self.color == piece.color