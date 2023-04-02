from Circle import *
from State import *
import numpy as np
import sys, pygame

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

    def handle_click(self, pos, board):
        clicked_circle = self.get_circle_from_pos(pos)
        if clicked_circle is None:
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


    def get_circle_from_pos(self, pos):
        for circle in self.circles:
            if circle.rect.collidepoint(pos):
                return circle
        return None

    def draw_board(self, board, display):
        if self.selected_piece is not None:
            for pos in board.piece_valid_moves(self.selected_piece.x, self.selected_piece.y):
                circle = self.get_circle_from_pos((57*pos[0] + 47, 58*pos[1] + 50))
                circle.highlight = True

        for circle in self.circles:
            circle.draw(display)

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