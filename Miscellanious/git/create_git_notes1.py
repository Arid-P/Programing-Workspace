# create_git_notes1.py
# This script generates Git notes as .bash files in the current directory

files = {
    "concepts.bash": """# =========================
# GIT — CORE CONCEPTS
# =========================

# Git is a DISTRIBUTED version control system.
# Distributed = every developer has the full history (no single point of failure).

# Git tracks:
# 1. Content (snapshots), not files
# 2. History as a Directed Acyclic Graph (DAG), not a straight line
# 3. Changes via hashes (SHA-1 / SHA-256 internally)

# Three main states of a file:
# 1. Working Directory  -> files you are editing
# 2. Staging Area       -> files prepared for commit
# 3. Repository (.git)  -> permanent history
""",

    "initialising.bash": """# =========================
# INITIAL SETUP
# =========================

git config --global user.name "Your Name"
# Sets author name for commits (metadata, not authentication)

git config --global user.email "you@email.com"
# Sets author email

git config --list
# Shows all git configuration values

# =========================
# INITIALIZING A REPO
# =========================

git init
# Creates a .git directory
# This folder IS the repository
# Delete .git -> project is no longer version-controlled

git status
# The most important command
# Shows:
# - current branch
# - staged files
# - unstaged files
# - untracked files
""",

    "tracking_add.bash": """# =========================
# TRACKING FILES
# =========================

git add file.txt
# Moves file from Working Directory -> Staging Area

git add .
# Stages ALL changes in current directory and subdirectories
# Dangerous if you don’t know what changed

git add -A
# Stages everything: new, modified, deleted files
# Safer when you want repo state = working directory state

git reset file.txt
# Unstages a file (Staging Area -> Working Directory)
""",

    "commit_cmd.bash": """# =========================
# COMMITTING CHANGES
# =========================

git commit -m "message"
# Creates a snapshot of the staged files
# Commit message should describe WHY, not WHAT

# BAD commit message:
# "fixed bug"

# GOOD commit message:
# "Fix division by zero error in calculator input validation"

git commit
# Opens editor for multi-line commit messages
# Used in serious projects

# =========================
# COMMIT HISTORY
# =========================

git log
# Shows commit history (hash, author, date, message)

git log --oneline
# Compact view, one commit per line

git log --graph --oneline --all
# Visualizes branching structure
# This teaches you more about Git than any tutorial
""",

    "branch_cmd.bash": """# =========================
# BRANCHES (CRITICAL)
# =========================

# A branch is NOT a copy of code.
# A branch is a POINTER to a commit.

git branch
# Lists branches

git branch new-feature
# Creates a new branch

git switch new-feature
# Switches to branch (modern, preferred)

git checkout new-feature
# Old way (does switching + other stuff, confusing)

git switch -c quick-fix
# Create + switch in one command
"""
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Git notes files created successfully.")