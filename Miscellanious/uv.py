"""
uv_notes.py
-----------
A complete reference guide for 'uv', the Rust-based Python environment and package manager.
Read the comments for detailed explanations of how it replaces pip and venv.
"""

import sys
import os

# =============================================================================
# 1. THE CORE CONCEPTS
# =============================================================================
# 'uv' replaces pip, pip-tools, and venv. 
# It is extremely fast because it uses a global cache. If you install 'numpy' 
# in 5 different projects, uv only downloads it once. It uses file system 
# hard-links to connect the cached version to your .venv instantly.

# =============================================================================
# 2. VIRTUAL ENVIRONMENTS (Replaces: python -m venv .venv)
# =============================================================================
# COMMAND: uv venv
# 
# What it does: Creates a standard PEP 405 virtual environment in the current 
# directory (defaults to a folder named `.venv`).
# 
# To activate it in your terminal:
#   source .venv/bin/activate
#
# To deactivate:
#   deactivate

# =============================================================================
# 3. PACKAGE MANAGEMENT (Replaces: pip install)
# =============================================================================
# COMMAND: uv pip install <package>
#
# What it does: Installs packages into the active virtual environment. 
# *Smart Feature:* If you are inside a project folder that contains a `.venv`, 
# `uv pip install` will automatically detect and install into that `.venv` 
# even if you forgot to activate it with 'source'!
#
# Examples:
#   uv pip install flask numpy         # Install multiple packages
#   uv pip install "pydantic>=2.0"     # Install specific versions
#   uv pip install -r requirements.txt # Install from a requirements file
#   uv pip list                        # Show installed packages

# =============================================================================
# 4. DEPENDENCY LOCKING (Replaces: pip freeze > requirements.txt)
# =============================================================================
# COMMAND: uv pip freeze > requirements.txt
# 
# What it does: Snapshots your exact current environment (all packages and 
# their exact versions) into a text file so you or someone else can recreate 
# the exact same environment later.

# =============================================================================
# 5. RUNNING SCRIPTS (The 'uv run' shortcut)
# =============================================================================
# COMMAND: uv run python_script.py
#
# What it does: You don't actually need to activate your environment to run 
# code. If you use `uv run my_code.py`, uv automatically finds the `.venv` in 
# your folder, activates it temporarily, runs the script, and closes it.


def is_running_in_venv():
    """
    Utility function to check if the current Python script is running 
    inside a virtual environment (like the one created by uv).
    """
    return sys.prefix != sys.base_prefix


def print_cheatsheet():
    """Prints a quick-reference guide to the terminal."""
    
    cheatsheet = """
=========================================================
                 UV COMMAND CHEATSHEET
=========================================================
Setup:
  uv venv                     -> Create a new .venv folder
  source .venv/bin/activate   -> Activate the environment

Install:
  uv pip install <pkg>        -> Install a package
  uv pip install -r req.txt   -> Install from requirements
  uv pip list                 -> View installed packages

Export:
  uv pip freeze > req.txt     -> Save dependencies to file

Execution:
  uv run script.py            -> Run script using the local .venv
                                 (no activation required!)
=========================================================
"""
    print(cheatsheet)
    
    if is_running_in_venv():
        print(f"[STATUS] You are currently running inside a virtual environment.")
        print(f"Environment Path: {sys.prefix}")
    else:
        print("[STATUS] You are running on the SYSTEM Python, NOT a virtual environment.")
        print("Run 'source .venv/bin/activate' and try again.")


if __name__ == "__main__":
    print_cheatsheet()