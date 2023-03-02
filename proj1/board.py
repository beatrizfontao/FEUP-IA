from piece import *

class Board:
    #Size must be odd
    def __init__(self, size):
        self.size = size
        self.numPieces = (size - 1)*2
        start = size // 2

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

        self.forbiddenCells = []
        for i in range(size):
            for j in range(size):
                if (i >= 0 and i < start - 1) or (i > start + 1 and i < size):
                    if (j >= 0 and j < start - 1) or (j > start + 1 and j < size):
                        cell = (i, j)
                        self.forbiddenCells.append(cell)

    def isCellEmpty(self, row, col):
        for obj in self.pieces:
            if obj.row == row and obj.col == col:
                return False
        return True
    
    def isCellForbidden(self, row, col):
        for (r,c) in self.forbiddenCells:
            if r == row and c == col:
                return True
        return False
    
    #TODO: add case for circular move
    def isPathEmpty(self, initRow, initCol, newRow, newCol):
        #Horizontal move
        if initRow == newRow:
            #Right
            if initCol < newCol:
                for i in range(initCol, newCol):
                    if not self.isCellEmpty(initRow, i):
                        print("right false")
                        return False
            #Left
            else:
                for i in range(newCol, initCol):
                    if not self.isCellEmpty(initRow, i):
                        print("left false")
                        return False
        #Vertical move
        elif initCol == newCol:
            #Down
            if initRow < newRow:
                print("down")
                for i in range(initRow + 1, newRow + 1):
                    print(i, initCol)
                    if not self.isCellEmpty(i, initCol):
                        print("down false")
                        return False
            #Up
            else:
                for i in range(newRow, initRow):
                    if not self.isCellEmpty(i, initCol):
                        print("up false")
                        return False
        #Circular move
        print("True")
        return True

    #TODO: check the player turn
    def validMove(self, piece, newCol, newRow):
        #check if the move is valid
        if piece.col == newCol and piece.row == newRow:
            print("Invalid move - same pos")
        elif self.isCellForbidden(newRow, newCol):
            print("Invalid move - forbidden move")
        else:
            if self.isPathEmpty(piece.row, piece.col, newRow, newCol):
                piece.move(newCol, newRow)
                print("Valid move")
            else:
                print("aaaaaa")
        #check if the path is free
    
    def printPieces(self):
        print("pieces: ")
        for obj in self.pieces:
            print(obj.row, obj.col)
            print(obj.color)
        #print("cells: ")
        #for obj in self.forbiddenCells:
        #    print(obj[0], obj[1]) 

#TEST
b = Board(9)
#print(b.numPieces)
#b.printPieces()
p = Piece(3,3,'black')
b.isPathEmpty(p.row, p.col, 4, 3)
#b.validMove(p, 3, 4)
#b.printPieces()