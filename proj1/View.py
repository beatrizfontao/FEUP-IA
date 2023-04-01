from Circle import *
from State import *
from Piece import *
import numpy as np
import sys, pygame

class View:
    # Size must be odd
    def __init__(self, size):

        self.size = size
        start = size // 2
        self.selected_piece = None

        forbidden_cells = []
        for i in range(size):
            for j in range(size):
                if (i >= 0 and i < start - 1) or (i > start + 1 and i < size):
                    if (j >= 0 and j < start - 1) or (j > start + 1 and j < size):
                        cell = (i, j)
                        forbidden_cells.append(cell)

        self.pieces = []
        for i in range(start-1, start + 3, 2):
            for j in range(size):
                if j >= 0 and j < start:
                    piece = Piece(i, j, 'player1')
                    self.pieces.append(piece)
                elif j >= start+1 and j < size:
                    piece = Piece(i, j, 'player2')
                    self.pieces.append(piece)

        # Create all circle
        self.circles = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                pos = (i, j)
                if pos not in forbidden_cells:
                    circle = Circle(pos[0], pos[1])
                    for piece in self.pieces:
                        if (piece.col, piece.row) == pos:
                            circle.occupying_piece = piece
                    self.circles.append(circle)

    def handle_click(self, pos, board):
        clicked_circle = self.get_circle_from_pos(pos)
        if clicked_circle is None:
            return

        if self.selected_piece is None:
            if clicked_circle.occupying_piece is not None:
                if clicked_circle.occupying_piece.player == board.turn:
                    self.selected_piece = clicked_circle.occupying_piece

        elif clicked_circle.occupying_piece is not None:
            if clicked_circle.occupying_piece.player == board.turn:
                self.selected_piece = clicked_circle.occupying_piece
                for circle in self.circles:
                    circle.highlight = False

        elif (board.handle_player_move(clicked_circle.y, clicked_circle.x, self.selected_piece.col, self.selected_piece.row)):
            self.get_circle_from_pos((self.selected_piece.screen_x, self.selected_piece.screen_y)).occupying_piece = None
            clicked_circle.occupying_piece = self.selected_piece
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
            for pos in board.piece_valid_moves(self.selected_piece.col, self.selected_piece.row):
                circle = self.get_circle_from_pos((57*pos[1] + 47, 58*pos[0] + 50))
                circle.highlight = True

        for circle in self.circles:
            circle.draw(display)
