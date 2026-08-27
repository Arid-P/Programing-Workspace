# content://com.android.externalstorage.documents/tree/primary%3APrograming::primary:Programing/Python/Projects/3 Number System Converter/conversion_utils/hexa_bin.py

import sys
def add_path_cwd() -> None:
    sys.path.append("/storage/emulated/0/Programing/Python/Projects/3 Number System Converter/conversion_utils/")  # Add current directory to sys.path
    return

if __name__ == "__main__":
    add_path_cwd()

import bin_deci as band
import hexa_deci as danh


def bina_to_hexa(bi: str) -> str:
    deci = band.bina_to_deci(bi)
    hex_ = danh.deci_to_hexa(str(deci))
    
    return hex_

def hexa_to_bina(hex_: str) -> str:
    deci = danh.hexa_to_deci(hex_)
    bi = band.deci_to_bina(str(deci))
    
    return bi

def main() -> None:
    bi = input("Enter a binary number: ")
    print(f"Binary to Hexadecimal: {bina_to_hexa(bi)}")
    
    hex_ = input("Enter a hexadecimal number: ")
    print(f"Hexadecimal to Binary: {hexa_to_bina(hex_)}")

if __name__ == "__main__":
    main()