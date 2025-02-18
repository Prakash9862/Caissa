import subprocess
import os

# Remplace par le chemin absolu de ton projet Caïssa
REPO_PATH = r"D:\Vincent\- Informatique -\Echecs OpenAi\Caissa"

# Message de commit
COMMIT_MESSAGE = "Mise à jour automatique"

def run_git_command(command, repo_path):
    """Exécute une commande Git dans le répertoire spécifié."""
    result = subprocess.run(["git"] + command, cwd=repo_path, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Erreur lors de l'exécution de {' '.join(command)} :\n{result.stderr}")
    else:
        print(result.stdout)

def main():
    if not os.path.isdir(REPO_PATH):
        print(f"Le chemin {REPO_PATH} n'existe pas ou n'est pas un répertoire.")
        return

    # Étapes Git
    print("Vérification des modifications...")
    run_git_command(["status"], REPO_PATH)

    print("Ajout des fichiers modifiés...")
    run_git_command(["add", "."], REPO_PATH)

    print("Validation des modifications...")
    run_git_command(["commit", "-m", COMMIT_MESSAGE], REPO_PATH)

    print("Envoi des modifications vers le dépôt distant...")
    run_git_command(["push"], REPO_PATH)

if __name__ == "__main__":
    main()
