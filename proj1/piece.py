import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, col, row, player):
        super().__init__()
        self.col = col
        self.row = row
        self.player = player
        if player == 'player1':
            self.image = pygame.image.load('piece.png').convert_alpha()
        else:
            self.image = pygame.image.load('pieceB.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.col, self.row))

    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow

    def is_equal(self, piece):
        return self.row == piece.row and self.col == piece.col and self.player == piece.player
