from Circle import *
from State import *
from Minimax import *
import pygame

class View:
    # Size must be odd
    def __init__(self, size, board):

        self.size = size
        self.selected_piece = None

        # Create all circle
        self.circles = []
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j] != -1):
                    circle = Circle(i, j)
                    circle.occupying_piece = board[i][j]
                    self.circles.append(circle)

    """
    Given the position of the click, this function recognizes if the player selected a piece, the hint icon or neither one.
    When the player clicks a piece, it highlights all the possible valid moves for that piece.
    When the player clicks the hint icon, it calls the minimax function and highlights a possible move.
    When the player doesn't click a piece or the hint icon, the click is ignored.
    """
    def handle_click(self, pos, board):
        clicked_circle = self.get_circle_from_pos(pos)
        
        if clicked_circle is None:
            hint_rect = pygame.Rect(530, 20, 45, 45) 
            if hint_rect.collidepoint(pos):
                _, piece, move = minimax(board, 3, -math.inf, math.inf, True, piece_enemy_moves)
                piece_circle = self.get_circle_from_pos((57*piece[0] + 47, 58*piece[1] + 50))
                move_circle = self.get_circle_from_pos((57*move[0] + 47, 58*move[1] + 50))

                piece_circle.highlight = True
                move_circle.highlight = True
                return
            else:
                return

        if self.selected_piece is None:
            if clicked_circle.occupying_piece != 0:
                if clicked_circle.occupying_piece == board.turn:
                    self.selected_piece = clicked_circle

        elif clicked_circle.occupying_piece != 0:
            if clicked_circle.occupying_piece == board.turn:
                self.selected_piece = clicked_circle
                for circle in self.circles:
                    circle.highlight = False

        elif (board.handle_player_move(clicked_circle.x, clicked_circle.y, self.selected_piece.x, self.selected_piece.y)):
            clicked_circle.occupying_piece = self.selected_piece.occupying_piece
            self.selected_piece.occupying_piece = 0
            self.selected_piece = None

        for circle in self.circles:
            circle.highlight = False

    """
    Given the position on the screen, this function returns the respective circle or None if there is no circle in said position.
    """
    def get_circle_from_pos(self, pos):
        for circle in self.circles:
            if circle.rect.collidepoint(pos):
                return circle
        return None

    """
    Draws each circle of the board and highlights the circles that contain valid moves for the selected piece
    """
    def draw_board(self, board, display):
        if self.selected_piece is not None:
            for pos in board.piece_valid_moves(self.selected_piece.x, self.selected_piece.y):
                circle = self.get_circle_from_pos((57*pos[0] + 47, 58*pos[1] + 50))
                circle.highlight = True

        for circle in self.circles:
            circle.draw(display)

    """
    Updates the View's circles so that, when a move occurs, the circle that had a piece now as no occupying piece
    And the circle that the piece was moved into has the player whose the piece belonged to in its occupying_piece variable
    """
    def update(self, row, col, new_row, new_col):
        counter = 0
        for c in self.circles:
            if c.x == row and c.y == col:
                circle = c
                counter += 1
            elif c.x == new_row and c.y == new_col:
                new_circle = c
                counter += 1
            if counter == 2: break
        new_circle.occupying_piece = circle.occupying_piece
        circle.occupying_piece = 0