# =========================
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
