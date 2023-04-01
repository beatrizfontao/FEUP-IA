import pygame

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.screen_x = 57*self.x + 47
        self.screen_y = 58*self.y + 50
        self.occupying_piece = None
        self.highlight = False
        self.highlight_color = (150, 255, 100)
        self.rect = pygame.Rect(
            self.screen_x,
            self.screen_y,
            self.width,
            self.height
        )

    def draw(self, display):
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        if self.occupying_piece == 1:
            image = pygame.image.load('piece.png').convert_alpha()
            display.blit(image, (self.screen_x, self.screen_y))
        elif self.occupying_piece == 2:
            image = pygame.image.load('pieceB.png').convert_alpha()
            display.blit(image, (self.screen_x, self.screen_y))