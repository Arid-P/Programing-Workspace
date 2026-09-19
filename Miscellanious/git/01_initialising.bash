# =========================
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
