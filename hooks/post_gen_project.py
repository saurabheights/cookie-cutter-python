#!/usr/bin/env python3
"""Post-generation hook: initialize a git repository with an initial commit."""

import subprocess
import sys

GITHUB_USERNAME = "{{ cookiecutter.github_host_username }}"
GITHUB_REPO = "{{ cookiecutter.github_repo_slug }}"


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def main() -> None:
    # Initialize repo with main as the default branch
    run(["git", "init", "-b", "main"])

    # Stage all generated files
    run(["git", "add", "."])

    # Create initial commit
    run(["git", "commit", "-m", "Initial commit"])

    # Set remote origin
    origin = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"
    run(["git", "remote", "add", "origin", origin])

    print(f"Git repository initialized on branch 'main'.")
    print(f"Remote origin set to: {origin}")
    print(f"Push with: git push -u origin main")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Error during git setup: {e.stderr}", file=sys.stderr)
        sys.exit(1)
