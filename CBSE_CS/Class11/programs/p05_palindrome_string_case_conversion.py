"""
Program 05: String Palindrome Check and Case Conversion
CBSE Class 11 Practical File

Objective:
1. Check whether a given string is a Palindrome (reads same forwards and backwards).
2. Convert and return a new string with swapped case (toggle uppercase to lowercase and vice-versa)
   without using the built-in swapcase() method.
"""


def is_palindrome(text: str) -> bool:
    # strin slicing too easy s == s[::-1]
    l, r = 0, len(text) - 1

    while l < r:
        if text[l] != text[r]:
            return False
        l += 1
        r -= 1

    return True


def toggle_case(text: str) -> str:
    str_new = ""

    for el in text:
        if not el.isalpha():
            str_new += el
            continue

        if ord(el) > 90:
            str_new += el.upper()
        else:
            str_new += el.lower()

    return str_new


if __name__ == "__main__":
    user_str = input("Enter a string: ")

    # 1. Palindrome Check
    if is_palindrome(user_str):
        print(f"'{user_str}' is a PALINDROME.")
    else:
        print(f"'{user_str}' is NOT a palindrome.")

    # 2. Case Conversion
    converted = toggle_case(user_str)
    print(f"Case-toggled string: '{converted}'")
