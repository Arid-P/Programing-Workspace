import sys

def add_path_cwd() -> None:
    sys.path.append("/storage/emulated/0/Programing/Python/Advance Basics/Modules and Packages/Your own M&P/Packages/")  # Add current directory to sys.path
    return

add_path_cwd()
from my_packages import math_operations as mo
from my_packages import string_operations as so

print(mo.add(3, 5))