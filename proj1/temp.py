import pygame, sys
from Piece import Piece
pygame.init()

background = pygame.image.load("a.png")
screen = pygame.display.set_mode((595, 600))

player = pygame.sprite.GroupSingle()
player.add(Piece(292, 80, 'black'))

clock = pygame.time.Clock()
screen.blit(background, (0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)
