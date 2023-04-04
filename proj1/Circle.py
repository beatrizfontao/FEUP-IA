import pygame
"""
Circle is an object that serves mainly as an hitbox for clicks and for highlighting the possible moves
"""
class Circle:
    def __init__(self, x, y):
        self.x = x #x coordinate in the state matrix
        self.y = y #y coordinate in the state matrix
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
        ) #pygame object that allows to click a piece and to draw the highlight

    # Draws the piece or displays the higlights (if a piece has been selected) and its occupying pieces
    def draw(self, display):
        if self.highlight:
            image = pygame.image.load('images/pieceHighlight.png').convert_alpha()
            display.blit(image, (self.screen_x, self.screen_y))
        # If the circle is occupied by player 1's piece, draw the player 1's respective image
        elif self.occupying_piece == 1:
            image = pygame.image.load('images/piece1.png').convert_alpha()
            display.blit(image, (self.screen_x, self.screen_y))
        # If the circle is occupied by player 2's piece, draw the player 2's respective image
        elif self.occupying_piece == 2:
            image = pygame.image.load('images/piece2.png').convert_alpha()
            display.blit(image, (self.screen_x, self.screen_y))