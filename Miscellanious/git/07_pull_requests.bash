# =========================
# PULL REQUESTS (PRs)
# =========================

# IMPORTANT:
# Pull Requests are NOT a Git feature.
# They are provided by platforms like GitHub, GitLab, Bitbucket.

# A Pull Request is a REQUEST to merge one branch into another
# Usually: feature branch -> main branch

# Why Pull Requests exist:
# - Code review before merging
# - Discussion and feedback
# - Automated checks (tests, linting, CI)
# - Prevent direct pushes to main

# =========================
# TYPICAL PR WORKFLOW
# =========================

# 1. Create a new branch
git switch -c feature-login

# 2. Make commits on that branch
git commit -m "Add login form validation"

# 3. Push branch to remote
git push origin feature-login

# 4. Open Pull Request on GitHub/GitLab UI
#    (NO Git command for this)

# 5. Review + approve
# 6. Merge PR using platform options

# =========================
# MERGE STRATEGIES IN PRs
# =========================

# Merge commit:
# - Preserves full branch history
# - Creates a merge commit

# Squash merge:
# - Combines all commits into ONE
# - Keeps main branch clean

# Rebase merge:
# - Rewrites history
# - Linear commit log
# - Dangerous if misunderstood

# =========================
# PRO TEAM RULE
# =========================

# Never push directly to main.
# If main is writable by everyone,
# your repo is already on fire.