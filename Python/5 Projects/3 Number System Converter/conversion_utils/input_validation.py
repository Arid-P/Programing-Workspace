# content://com.android.externalstorage.documents/tree/primary%3APrograming::primary:Programing/Python/Projects/3 Number System Converter/conversion_utils/input_validation.py

def is_zero (numstr: str) -> bool :
    check_set = set([chr_ for chr_ in numstr])
    if check_set == {'0'} :
        return True
    
    return False

def is_binary(bi: str) -> str:
    if not bi.isdigit():
        print("Please enter a valid integral value")
        return take_input("bi")
    
    check: set = {chr_ for chr_ in bi}
    if check not in [{'0', '1'}, {'1', '0'}, {'1'}, {'0'}]:
        print("Enter a valid binary value")
        return take_input("bi")
    
    return bi


def is_decimal (dec: str) -> bool :
    try :
        dec = int(dec)
    except ValueError :
        return take_input("dec")
    
    return str(dec)


def is_hex(hex_: str) -> str:
    check_list = [chr_ for chr_ in hex_]
    
    hex_chrs = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    
    result: bool = all([ chr_ in hex_chrs for chr_ in check_list ])
    if not result :
        return take_input("hex_")
    return str(hex_)


def valid_choice (choice_no: str) -> str :
    choice_no = is_decimal(choice_no)
    
    if int(choice_no) < 1 or int(choice_no) > 6 :
        return take_input("choice")
    
    return int(choice_no)


def take_input (func_name: str) -> str :
    if func_name == "choice" :
        ip = input("Enter the appropriate choice:  ")
        return valid_choice(ip)
    
    ip = input("Enter the appropriate value:  ")
    
    if func_name == "bi" :
        return is_binary(ip)
    elif func_name == "dec" :
        return is_decimal(ip)
    elif func_name == "hex_" :
        return is_hex(ip)



def main () -> None :
    #raise ValueError('main not implemented')
    n = input("Enter a hex value:  ")
    print(is_hex(n))
    n = input("Enter a binary value:  ")
    print(is_binary(n))
    n = input("Enter a decimal value:  ")
    print(is_decimal(n))
    n = input("Enter a choice value:  ")
    print(valid_choice(n))
    n = input("Enter a zero:  ")
    print(is_zero(n))
    
    return

if __name__ == "__main__" :
    main()