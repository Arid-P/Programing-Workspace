from collections import Counter


def input_str() -> str:
    """
    input_str: inputs the string with input validation.
    
    Returns:
    str: the entered string with leading and trailing whitespace removed.
    """
    
    while True:
      string = input('Enter the string: ')
        
      if not string.replace(" " , "").isalpha():
        print("Please enter a valid string containing only alphabetic characters.")
      else:
        return string


def main() -> None:
    """
    main: counts occurrences of characters in the string (ignoring spaces), sorts the characters
    by frequency in descending order, and prints the character with the highest frequency.
    
    Returns:
    None: prints the most frequent character and its count.
    """
    string = input_str()
    
    # Count characters excluding spaces
    chr_w_ocurrences = Counter(string).items()
    
    # Sort by occurrence in descending order
    chr_w_ocurrences = sorted(chr_w_ocurrences, key=lambda chr_ocurr: -chr_ocurr[1])
    
    # Print the most frequent character
    return print(f"The most frequent character is '{chr_w_ocurrences[0][0]}' with a count of {chr_w_ocurrences[0][1]}.")


if __name__ == "__main__":
    main()