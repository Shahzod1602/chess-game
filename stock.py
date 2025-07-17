from stockfish import Stockfish

stockfish = Stockfish(
    path="stockfish-windows-x86-64-avx2.exe",  # yoki Linuxda "/usr/games/stockfish"
    depth=15,
    parameters={"Threads": 2, "Minimum Thinking Time": 30}
)
