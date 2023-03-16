import pygame, sys
from Board import Board
pygame.init()

#Screen and Background
screen = pygame.display.set_mode((595, 600))
background = pygame.image.load("a.png")

board = Board(9)

def draw(display):
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    board.draw(display)
    pygame.display.update()

while True:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.handle_click(pos)

    i = board.is_game_over()
    if i != 0:
        print("player " + str(i) + " won!")
        sys.exit()
    draw(screen)
