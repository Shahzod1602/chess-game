import pygame
from board import ChessBoard

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Chess.com Style Chess")

board_ui = ChessBoard(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        board_ui.handle_event(event)

    board_ui.draw()
    pygame.display.flip()
