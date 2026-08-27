# =========================
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
