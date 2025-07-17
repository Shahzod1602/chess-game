import pygame
import chess
import os
from logic import square_to_coords, coords_to_square
from stock import stockfish

class ChessBoard:
    def __init__(self, screen):
        self.screen = screen
        self.board = chess.Board()
        self.selected_square = None
        self.images = self.load_images()
        self.square_size = 80

    def load_images(self):
        pieces = ['wp', 'wr', 'wn', 'wb', 'wq', 'wk',
                  'bp', 'br', 'bn', 'bb', 'bq', 'bk']
        images = {}
        for piece in pieces:
            path = os.path.join("assets", "figures", f"{piece}.png")
            images[piece] = pygame.transform.scale(pygame.image.load(path), (80, 80))
        return images

    def draw(self):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for rank in range(8):
            for file in range(8):
                color = colors[(rank + file) % 2]
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(file * 80, rank * 80, 80, 80)
                )

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                symbol = piece.symbol()
                prefix = 'w' if symbol.isupper() else 'b'
                image_key = prefix + symbol.lower()
                x, y = square_to_coords(square)
                self.screen.blit(self.images[image_key], (x, y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            clicked_square = coords_to_square(x, y)
            piece = self.board.piece_at(clicked_square)

            if self.selected_square is None:
                if piece:
                    self.selected_square = clicked_square
            else:
                move = chess.Move(self.selected_square, clicked_square)
                if move in self.board.legal_moves:
                    self.board.push(move)
                    stockfish.set_fen_position(self.board.fen())
                    print("Best move:", stockfish.get_best_move())
                self.selected_square = None
