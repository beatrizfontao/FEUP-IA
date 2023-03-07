import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, col, row, color):
        super().__init__()
        self.col = col
        self.row = row
        self.color = color
        if color == 'white':
            self.image = pygame.image.load('piece.png').convert_alpha()
        else:
            self.image = pygame.image.load('pieceB.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.col, self.row))

    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow

    def is_equal(self, piece):
        return self.row == piece.row and self.col == piece.col and self.color == piece.color

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.MOUSEBUTTONDOWN] and self.rect.collidepoint(keys[pygame.MOUSEBUTTONDOWN].pos):
            print("something")
