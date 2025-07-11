
from git import Repo
def clone_repo(repo_url, dest_dir="./cloned_repo"):
    Repo.clone_from(repo_url, dest_dir)
    print(f"Repo cloned to {dest_dir}")

