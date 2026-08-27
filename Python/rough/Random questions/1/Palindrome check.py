def is_palindrome(text: str) -> bool:
    half_len = int(len(text) / 2)
    #print(half_len)

    # if len(text) % 2 != 0 :
#         for i in range(1, half_len+1) :
#             #print(f"{i=},  {text[half_len - i]=} {text[half_len + i]=}")
#             if text[half_len - i] != text[half_len + i] :
#                 return False
#     else :
#         for i in range(0, half_len) :
#             #print(f"{i=},  {text[half_len - 1 - i]=} {text[half_len + i]=}")
#             if text[half_len - 1 - i] != text[half_len + i] :
#                 return False

    for i in range(0, half_len) :
        if text[i] != text[-1 * (i + 1)] :
            return False

    return True

def main () -> None :
    text = input("Enter Text: ")
    
    if is_palindrome(text) :
        print(f"{text} is palindrome")
    else :
        print(f"{text} is not palindrome")
        
    return

if __name__ == "__main__" :
    main()