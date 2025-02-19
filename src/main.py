from load_games import load_pgn_games

# Charger les parties au démarrage
games = load_pgn_games()
print(f"📂 {len(games)} parties chargées dans Caïssa !")

from stockfish import Stockfish

# Assure-toi que ce chemin correspond bien à l'exécutable Stockfish dans assets/
stockfish_path = r"D:\Vincent\- Informatique -\Echecs OpenAi\stockfish\stockfish-windows-x86-64-avx2.exe"

class ChessEngine:
    def __init__(self, stockfish_path):
        self.stockfish = Stockfish(stockfish_path)

    def is_ready(self):
        return self.stockfish.is_ready()

    def get_best_move(self, position=None):
        if position:
            self.stockfish.set_fen_position(position)
        return self.stockfish.get_best_move()

# Test rapide
if __name__ == "__main__":
    engine = ChessEngine(stockfish_path)
    print("Stockfish ready:", engine.is_ready())
    print("Best move for starting position:", engine.get_best_move())
 
