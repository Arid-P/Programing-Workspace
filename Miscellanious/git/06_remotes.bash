# =========================
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
