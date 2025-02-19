import os
import chess.pgn
import tkinter as tk
from tkinter import ttk, scrolledtext

# Chemin des parties
PARTIES_PATH = r"D:\Vincent\- Informatique -\Echecs OpenAi\automatisation_chess\sorted_chess_games"

def load_pgn_games():
    """Charge les parties PGN depuis sorted_chess_games."""
    games = []
    game_files = []
    
    for root, _, files in os.walk(PARTIES_PATH):
        for file in files:
            if file.endswith(".pgn"):
                file_path = os.path.join(root, file)
                game_files.append(file_path)
    
    return game_files

def display_game(event):
    """Affiche le contenu PGN de la partie sélectionnée."""
    selected_index = listbox.curselection()
    if not selected_index:
        return
    
    file_path = game_files[selected_index[0]]
    with open(file_path, "r", encoding="utf-8") as f:
        pgn_content = f.read()
    
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, pgn_content)
    text_area.config(state=tk.DISABLED)

# Charger les parties
game_files = load_pgn_games()

# Création de la fenêtre principale
root = tk.Tk()
root.title("📂 Sélecteur de Parties d'Échecs")

# Listbox pour afficher les parties disponibles
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

listbox = tk.Listbox(frame, height=20, width=50)
listbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

listbox.config(yscrollcommand=scrollbar.set)

# Ajouter les parties dans la liste
for file in game_files:
    listbox.insert(tk.END, os.path.basename(file))

# Zone de texte pour afficher le contenu PGN
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_area.grid(row=1, column=0, padx=10, pady=10)
text_area.config(state=tk.DISABLED)

# Lier l'événement de sélection à l'affichage du contenu
listbox.bind("<<ListboxSelect>>", display_game)

# Lancer l'interface
root.mainloop()
