# =========================
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
