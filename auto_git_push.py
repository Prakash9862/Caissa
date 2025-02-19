import os
import subprocess
import sys

# Répertoire du projet Caïssa (à ajuster si nécessaire)
PROJECT_DIR = r"D:\Vincent\- Informatique -\Echecs OpenAi\Caissa"

# Messages de commit automatique
COMMIT_MESSAGE = "Auto-commit: mise à jour automatique du projet Caïssa"

def run_command(command, cwd=PROJECT_DIR):
    """Exécute une commande shell et affiche la sortie."""
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        sys.stderr.write(result.stderr + "\n")

def auto_git_push():
    """Automatise le commit et le push du projet Caïssa."""
    try:
        print("🚀 Vérification des changements...")
        run_command("git add .")
        run_command(f'git commit -m "{COMMIT_MESSAGE}"')
        run_command("git push origin main")
        print("✅ Push réussi sur GitHub !")
    except Exception as e:
        sys.stderr.write(f"❌ Erreur lors du push : {e}\n")

if __name__ == "__main__":
    auto_git_push()
