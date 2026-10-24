# content://com.android.externalstorage.documents/tree/primary%3APrograming::primary:Programing/Python/Projects/3 Number System Converter/conversion_utils/hexa_deci.py

def hexa_to_deci(hex_: str) -> int | None:
    alphabet_num = {
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    
    hex_ = hex_[::-1]
    deci: int = 0
    for i in range(len(hex_)):
        if hex_[i].isalpha():
            num = alphabet_num[hex_[i]]
        else:
            num = int(hex_[i])
        deci += num * 16 ** abs(i)
    
    return deci


def deci_to_hexa(deci: str) -> str | None:
    if not deci.isdigit():
        print("Please enter a valid integral value")
        return None
    
    deci = int(deci)
    num_alphabet = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    remi: list = []
    
    while deci >= 1:
        rem = deci % 16
        deci = int(deci / 16)
        if rem <= 9:
            remi.append(str(int(rem)))
        else:
            remi.append(num_alphabet[int(rem)])
    
    remi.reverse()
    return ''.join(remi)


def main() -> None:
    hex_ = input("Enter a hexadecimal number: ")
    print(f"Hexadecimal to Decimal: {hexa_to_deci(hex_)}")
    
    deci = input("Enter a decimal number: ")
    print(f"Decimal to Hexadecimal: {deci_to_hexa(deci)}")

if __name__ == "__main__":
    main()