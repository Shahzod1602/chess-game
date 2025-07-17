import chess

def square_to_coords(square):
    file = chess.square_file(square)
    rank = 7 - chess.square_rank(square)
    return file * 80, rank * 80

def coords_to_square(x, y):
    file = x // 80
    rank = 7 - (y // 80)
    return chess.square(file, rank)
