# content://com.android.externalstorage.documents/tree/primary%3APrograming::primary:Programing/Python/Projects/3 Number System Converter/conversion_utils/bin_deci.py

def bina_to_deci(bi: str) -> int | None:
    num: int = 0
    for i in range(-1, -len(bi) - 1, -1):
        num += int(bi[i]) * 2 ** (abs(i) - 1)
    
    return num


def deci_to_bina(deci: str) -> str | None:
    n = int(deci)
    rem: list = []
    
    while n >= 1:
        rem.append(str(n % 2))
        n = int(n / 2)
    
    rem.reverse()
    return ''.join(rem)



def main() -> None:
    bi = input("Enter a binary number: ")
    print(f"Binary to Decimal: {bina_to_deci(bi)}")
    
    deci = input("Enter a decimal number: ")
    print(f"Decimal to Binary: {deci_to_bina(deci)}")

if __name__ == "__main__":
    main()