

def input_text() -> str:
    """
    input_text: Inputs the text and checks if it is valid or not.

    Returns:
    str: The input text.
    """
    while True:
        text: str = input("Enter the text: ")
        if not text.isalpha():
            print('Enter a valid text (alphabetic characters only)')
        else:
            break
    return text


def xyz (el: list) -> list :
  el[1] = str( el[1] )
  return el

def creating_new_text(chr_count: list[list]) -> str:
    """
    creating_new_text: This function could potentially process the 
    character counts in some way and generate a new representation.
    For now, it's a placeholder for future logic.

    Args:
    chr_count (list[tuple]): A list of tuples where each tuple containsa character and its count.
    """
    # Placeholder for actual functionality if needed.
    shorter_text = ""
    
    for el in chr_count :
      el[1] = str( el[1] )
      peice = ''.join(el)
      shorter_text += peice
      
    return shorter_text


def counting(text: str) -> list[list]:
    """
    counting: Counts occurrences of consecutive characters in the text
    
    Args:
    text (str): The input text.

    Returns:
    list[tuple]: A list of tuples where each tuple contains a character and its count in a consecutive sequence.
    """
    chr_count: list[tuple] = []
    count = 1  # Initializing count for the first character
    
    for i in range(1, len(text)):
      if text[i] == text[i - 1]:
        count += 1  # Increment count for consecutive characters
      else:
        # Append the current character and its count
        chr_count.append([text[i - 1], count])
        count = 1  # Reset count for the new character
    
    # Append the last character and its count
    chr_count.append([text[-1], count])

    return chr_count


def main() -> None:
    """
    main: The main function that controls the flow of the program.
    It reads the input text, counts the character occurrences, and prints the result.
    """
    text = input_text()  # Uncomment to take input from the user
    
    # Count the consecutive characters
    chr_count: list[tuple] = counting(text)
    
    #checking if the shorter text is actuallupy shorter or not
    if len(chr_count) >= len(text)/2 :
      return print(text)
      
    # Print the character counts
    print(creating_new_text(chr_count))


if __name__ == "__main__":
    main()
    main()
    main()