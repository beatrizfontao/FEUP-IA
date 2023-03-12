import pygame

class Piece():
    def __init__(self, col, row, player):
        self.col = col
        self.row = row
        self.screen_x = 57*self.col + 47
        self.screen_y = 58*self.row + 50
        self.player = player
        if player == 'player1':
            self.image = pygame.image.load('piece.png').convert_alpha()
        else:
            self.image = pygame.image.load('pieceB.png').convert_alpha()

    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow
        self.screen_x = 57*self.col + 47
        self.screen_y = 58*self.row + 50

    def is_equal(self, piece):
        return self.row == piece.row and self.col == piece.col and self.player == piece.player
