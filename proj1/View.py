from Circle import *
from State import *
from Piece import *
import numpy as np
import sys, pygame

class View:
    # Size must be odd
    def __init__(self, size, board):

        self.size = size
        start = size // 2
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
        #print('handle click')

        clicked_circle = self.get_circle_from_pos(pos)
        if clicked_circle is None:
            #print('clicked circle none')
            return

        if self.selected_piece is None:
            if clicked_circle.occupying_piece != 0:
                if clicked_circle.occupying_piece == board.turn:
                    #print('right turn')
                    self.selected_piece = clicked_circle

        elif clicked_circle.occupying_piece != 0:
            if clicked_circle.occupying_piece == board.turn:
                #print('right turn!!!!!!!')
                self.selected_piece = clicked_circle
                for circle in self.circles:
                    circle.highlight = False

        elif (board.handle_player_move(clicked_circle.x, clicked_circle.y, self.selected_piece.x, self.selected_piece.y)):
            #print('handle player move')
            clicked_circle.occupying_piece = self.selected_piece.occupying_piece
            self.selected_piece.occupying_piece = 0
            self.selected_piece = None

        for circle in self.circles:
            circle.highlight = False


    def get_circle_from_pos(self, pos):
        print(pos)
        for circle in self.circles:
            if circle.rect.collidepoint(pos):
                #print('collide')
                #print(circle.screen_x, circle.screen_y)
                return circle
        return None

    def draw_board(self, board, display):
        if self.selected_piece is not None:
            for pos in board.piece_valid_moves(self.selected_piece.col, self.selected_piece.row):
                circle = self.get_circle_from_pos((57*pos[1] + 47, 58*pos[0] + 50))
                circle.highlight = True

        for circle in self.circles:
            circle.draw(display)
