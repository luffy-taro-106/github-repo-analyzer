
from ingest.fetch_repo import clone_repo
from ui.interface import run_terminal_qa

if __name__ == "__main__":
    repo_url = input("Enter GitHub repo URL to analyze: ")
    clone_repo(repo_url)
    run_terminal_qa()

