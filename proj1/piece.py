import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, col, row, color):
        super().__init__()
        self.col = col
        self.row = row
        self.color = color
        self.image = pygame.image.load('piece.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.col, self.row))

    def move(self, newCol, newRow):
        self.col = newCol
        self.row = newRow
