# =========================
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
