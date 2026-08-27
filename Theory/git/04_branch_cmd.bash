# =========================
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
