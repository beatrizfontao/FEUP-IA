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
    
    def verticalPathEmpty(self, col, initRow, newRow):
        #Down
        if initRow < newRow:
            start = initRow + 1
            end = newRow + 1
        #Up
        else:
            start = newRow
            end = initRow
        for i in range(start, end):
            if not self.isCellEmpty(i, col):
                print("up false")
                return False
        return True
            
    def horizontalPathEmpty(self, row, initCol, newCol):
        #Right
        if initCol < newCol:
            start = initCol
            end = newCol
        #Left
        else:
            start = newCol
            end = initCol
        for i in range(start, end):
            if not self.isCellEmpty(row, i):
                print("Horizontal path not empty")
                return False  
        return True

    #TODO: add case for circular move
    def isPathEmpty(self, initRow, initCol, newRow, newCol):
        #Horizontal move
        if initRow == newRow:
            if self.horizontalPathEmpty(initRow, initCol, newCol):
                return True
        #Vertical move
        elif initCol == newCol:
            if self.verticalPathEmpty(initCol, initRow, newRow):
                return True

        #Circular move
        if initRow == newCol: 
            #meio de cima para esquerda
            if initRow < self.center:
                #ver se a horizontal e vertical estao vazias
                if self.horizontalPathEmpty(initRow, initCol, self.center) and self.verticalPathEmpty(newCol, self.center, newRow):
                    return True
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
            elif initRow > self.center + 2:
                return False

            

    #Checks if the move chosen is valid. Return True if it is and False otherwise
    def validMove(self, piece, newCol, newRow):
        #check if the move is valid
        if piece.col == newCol and piece.row == newRow:
            print("Invalid move - same pos")
            return False
        elif self.isCellForbidden(newRow, newCol):
            print("Invalid move - forbidden move")
            return False
        else:
            if self.isPathEmpty(piece.row, piece.col, newRow, newCol):
                print("Valid move")
                return True
            else:
                return False
    
    #Checks if the chosen move is valid and moves the piece. Returns true if the move is valid and false otherwise.
    def movePiece(self, initRow, initCol, color, newCol, newRow):
        canPlay = False
        for piece in self.pieces:
            if piece.row == initRow and piece.col == initCol:
                #Check turn
                if piece.color == color:
                    canPlay = True
                    p = piece
                else:
                    print("You can't move the other player's piece.")
                    return False
        if self.validMove(p, newCol, newRow) and canPlay:
            p.move(newCol, newRow)
            return True
        else:
            print("Invalid move!")
            return False

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
#b.isPathEmpty(p.row, p.col, 4, 3)
b.movePiece(3,3,'white',3,4)
#b.validMove(p, 3, 4)
b.printPieces()