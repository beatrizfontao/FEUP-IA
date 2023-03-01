class Piece:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
    
    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow