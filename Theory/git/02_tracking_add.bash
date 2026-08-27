# =========================
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
