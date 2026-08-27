# create_git_notes2.py
# Generates Git notes as .bash files in the current directory

files = {
    "merging_cloning.bash": """# =========================
# MERGING
# =========================

git merge new-feature
# Merges new-feature into current branch

# Fast-forward merge:
# - No divergence
# - Just moves branch pointer forward

# Merge commit:
# - Happens when histories diverge
# - Creates a new commit tying histories together

# =========================
# CLONING
# =========================

git clone https://github.com/user/repo.git
# Copies entire repository with full history
""",

    "remotes.bash": """# =========================
# REMOTES (GITHUB / GITLAB)
# =========================

git remote -v
# Shows remote repositories

git remote add origin https://github.com/user/repo.git
# Adds remote named "origin"

git push origin main
# Pushes local main branch to remote

git pull origin main
# Fetch + merge in one step
# Can cause surprises

git fetch origin
# Downloads changes WITHOUT merging
# Safer, more professional
""",

    "fixing_mistakes.bash": """# =========================
# FIXING MISTAKES
# =========================

git checkout -- file.txt
# Discards changes in working directory
# WARNING: irreversible

git reset --soft HEAD~1
# Undo last commit, keep changes staged

git reset --mixed HEAD~1
# Undo last commit, keep changes unstaged (default)

git reset --hard HEAD~1
# Nuclear option
# Deletes commit AND changes completely
""",

    "gitignore_rest_theory.bash": """# =========================
# .gitignore
# =========================

# Files listed here are NOT tracked
# Examples:
# node_modules/
# __pycache__/
# .env
# *.log

# Important:
# Git ignores files ONLY if they were never tracked

# =========================
# MAIN vs MASTER (IMPORTANT THEORY)
# =========================

# Historically:
# The default branch name was "master"

# Problems:
# - Ambiguous meaning
# - Cultural baggage
# - Not descriptive

# Modern standard:
# Default branch = "main"

# GitHub changed default to "main" in 2020

# TECHNICALLY:
# There is ZERO difference between main and master
# They are just names

# Why you still see "master":
# 1. Old repositories
# 2. Old Git versions
# 3. Legacy tooling

# Best practice today:
# Use "main" for new projects

# =========================
# MENTAL MODEL (THIS MAKES YOU DANGEROUS)
# =========================

# Git does NOT store diffs.
# Git stores snapshots.

# Commits form a graph.
# Branches are pointers.
# HEAD points to your current branch.
# Hashes identify exact states.

# If you understand this,
# Git stops being scary.
"""
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Additional Git notes files created successfully.")