import subprocess
from datetime import datetime

README_PATH = "README.md"

def get_git_log():
    """Récupère les 5 derniers commits pour afficher l'historique."""
    result = subprocess.run(["git", "log", "--oneline", "--graph", "--all", "-n", "5"], capture_output=True, text=True)
    return result.stdout.strip()

def get_project_status():
    """Génère le contenu mis à jour du README.md."""
    status = f"""
# 📌 Projet Caïssa - Suivi en Temps Réel

🛠️ **État actuel du projet :**
- ✔ Importation et stockage des parties **OK**
- ✔ Synchronisation GitHub automatique **OK**
- 🔄 **Stockfish en cours d'intégration**
- 🔄 **Interface graphique en développement**
- 🛠 **Notifications en phase de test**

📅 **Mise à jour automatique :** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 🔄 Derniers commits :
```
{get_git_log()}
```

## 💾 Comment utiliser le projet ?
```bash
python main.py  # Lancer Caïssa
python send_all_games_to_api.py  # Envoyer les parties à l'API
git sync  # Sauvegarde et mise à jour GitHub
```

🔄 **Ce fichier est mis à jour automatiquement après chaque commit.**
"""
    return status

def update_readme():
    """Met à jour le README.md avec l'état actuel du projet."""
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(get_project_status())
    
    print("✅ README.md mis à jour avec succès.")

def commit_and_push():
    """Ajoute, commit et pousse automatiquement le README.md"""
    subprocess.run(["git", "add", "README.md"])
    subprocess.run(["git", "commit", "-m", "🔄 Mise à jour automatique du README.md"], check=True)
    subprocess.run(["git", "push", "origin", "master"], check=True)

if __name__ == "__main__":
    update_readme()
    commit_and_push()
