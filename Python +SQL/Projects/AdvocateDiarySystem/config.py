# config.py
"""
Central configuration file for Advocate Diary System.

All paths and environment-level settings live here.
No hardcoded paths should appear elsewhere in the project.
"""

from pathlib import Path

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# Backend paths
BACKEND_DIR = BASE_DIR / "backend"
DB_DIR = BACKEND_DIR / "db"

# Global database
MAIN_DB_PATH = DB_DIR / "dairy.sqlite"

# Per-advocate DB folder template
ADVOCATE_DB_DIR = DB_DIR  # advocate_id folders created inside this

# SQLite connection settings
SQLITE_ECHO = False  # Set True for debugging SQL queries

# Date format standards
DATE_FORMAT = "%Y-%m-%d"

# Logging
LOG_LEVEL = "INFO"
LOG_DIR = BASE_DIR / "logs"
