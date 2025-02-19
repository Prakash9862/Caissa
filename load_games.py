import os
import chess.pgn

# Chemin vers les parties triées
PARTIES_PATH = r"D:\Vincent\- Informatique -\Echecs OpenAi\automatisation_chess\sorted_chess_games"

def load_pgn_games():
    """Parcourt les sous-dossiers et charge les parties PGN."""
    all_games = []
    
    for root, _, files in os.walk(PARTIES_PATH):
        for file in files:
            if file.endswith(".pgn"):
                file_path = os.path.join(root, file)
                with open(file_path, encoding="utf-8") as pgn:
                    game = chess.pgn.read_game(pgn)
                    if game:
                        all_games.append(game)
    
    print(f"✅ {len(all_games)} parties chargées depuis {PARTIES_PATH}")
    return all_games

# Test rapide
if __name__ == "__main__":
    load_pgn_games()
