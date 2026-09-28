# content://com.android.externalstorage.documents/tree/primary%3APrograming::primary:Programing/Python/Projects/3 Number System Converter/main.py

def add_path_cwd() -> None:
    import sys
    sys.path.append("/storage/emulated/0/Programing/Python/Projects/3 Number System Converter/conversion_utils/")  # Add current directory to sys.path
    return

if __name__ == "__main__" :
    add_path_cwd()
    import bin_deci as bd
    import hexa_deci as dh
    import hexa_bin as bh
    import input_validation as iv


def main () -> None :
    print("1. Binary to Decimal")
    print("2. Binary to Hexadecimal")
    print("3. Decimal to Binary")
    print("4. Decimal to Hexadecimal")
    print("5. Hexadecimal to Binary")
    print("6. Hexadecimal to Decimal")
    print()
    print("Chose which converstion do you want by type the number in its start.")
    print()
    choice: str = input("Enter the choice number:  ")
    choice: int = iv.valid_choice(choice)
    
    print()
    value: str = input("Enter the value to be converted:  ")
    print()
    
    if iv.is_zero(value) :
        print("After converstion it will only remain 0")
    if choice == 1 :
        value = iv.is_binary(value)
        result = bd.bina_to_deci(value)
        result_text = f"Binary value: {value}  -->  Decimal value: {result}"
    
    elif choice == 2 :
        value = iv.is_binary(value)
        result = bh.bina_to_hexa(value)
        result_text = f"Binary value: {value}  -->  Hexadecimal value: {result}"
    
    elif choice == 3 :
        value = iv.is_decimal(value)
        result = bd.deci_to_bina(value)
        result_text = f"Decimal value: {value}  -->  Binary value: {result}"
    
    elif choice == 4 :
        value = iv.is_decimal(value)
        result = dh.deci_to_hexa(value)
        result_text = f"Decimal value: {value}  -->  Hexadecimal value: {result}"
    
    elif choice == 5 :
        value = iv.is_hex(value)
        result = bh.hexa_to_bina(value)
        result_text = f"Hexadecimal value: {value}  -->  Binary value: {result}"
    
    elif choice == 6 :
        value = iv.is_hex(value)
        result = dh.deci_to_bina(value)
        result_text = f"Hexadecimal value: {value}  -->  Decimal value: {result}"
    
    
    print(result_text)
    print()
    
    

if __name__ == "__main__" :
    main()

