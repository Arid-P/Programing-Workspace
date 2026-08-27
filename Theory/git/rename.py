# prefix_git_notes.py
# Adds numeric prefixes to Git notes files in learning order

import os

ordered_files = [
    ("concepts.bash", "00_concepts.bash"),
    ("initialising.bash", "01_initialising.bash"),
    ("tracking_add.bash", "02_tracking_add.bash"),
    ("commit_cmd.bash", "03_commit_cmd.bash"),
    ("branch_cmd.bash", "04_branch_cmd.bash"),
    ("merging_cloning.bash", "05_merging_cloning.bash"),
    ("remotes.bash", "06_remotes.bash"),
    ("pull_requests.bash", "07_pull_requests.bash"),
    ("fixing_mistakes.bash", "08_fixing_mistakes.bash"),
    ("gitignore_rest_theory.bash", "09_gitignore_rest_theory.bash"),
]

for old_name, new_name in ordered_files:
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"Skipped (not found): {old_name}")

print("Renaming complete.")