import pygame, sys
from Piece import Piece
from Board import Board
pygame.init()

#Screen and Background
screen = pygame.display.set_mode((595, 600))
background = pygame.image.load("a.png")
screen.blit(background, (0,0))

board = Board(9)
pieces = pygame.sprite.Group()

for piece in board.pieces:
    pieces.add(piece)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pieces.draw(screen)
    pygame.display.update()
    clock.tick(60)
