def into_ascii_chr(final_values: list[int]) -> None:
    """
    Converts the final ASCII values to characters and replaces invalid symbols
    with lowercase letters based on the ASCII value modulus 26.
    """
    # Convert the ASCII values to characters
    chars = [chr(value) for value in final_values]
    
    # Define the updated allowed symbols set
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!;:\'"*/)(+-&_$#@][%\}{=^|`~.')

    # Replace invalid symbols with lowercase letters
    for i, char in enumerate(chars):
        if char not in allowed_chars:
            # If the character is not allowed, replace it with a letter
            ascii_value = ord(char)
            mod_value = ascii_value % 26  # Get the modulus value
            replacement_char = chr(ord('a') + mod_value)  # Get the corresponding letter
            chars[i] = replacement_char  # Replace the character

    # Join and print the final result string
    result_string = "".join(chars)
    return result_string


def process_string(input_str: str) -> list[int]:
    """
    Processes each character of the input string by converting its ASCII value 
    into specific bases (8, 10, 16) with additional transformations as described.

    Args:
      input_str (str): The string to process.

    Returns:
      list[int]: A list of converted values based on the given transformations.
    """
    converted_values = []

    # Iterate over each character and its index in the input string
    for index, char in enumerate(input_str):
        ascii_value = ord(char)  # Get ASCII value of the character

        if index % 3 == 0:  # Base 8 conversion for every 1st character in a set of 3
            base_8 = oct(ascii_value)[2:]  # Convert to base 8 (remove the '0o' prefix)
            if len(base_8) == 3:  # Apply the two-digit transformation if 3 digits
                part1 = int(base_8[0]) + int(base_8[1])
                part2 = int(base_8[1]) + int(base_8[2])
                final_base_8 = int(f"{part1}{part2}")
            else:
                final_base_8 = int(base_8)  # Keep as is if not 3 digits
            converted_values.append(final_base_8)

        elif index % 3 == 1:  # Base 10 for every 2nd character in a set of 3
            converted_values.append(ascii_value)

        elif index % 3 == 2:  # Base 16 for every 3rd character in a set of 3
            base_16 = hex(ascii_value)[2:]  # Convert to base 16 (remove the '0x' prefix)
            if base_16.isdigit():  # If it's purely numeric
                converted_values.append(int(base_16))
            else:  # If it contains a letter (like 'D')
                # Take the ASCII value of the letter (last character in hex)
                letter_ascii = ord(base_16[-1].upper())  # ASCII value of the letter and upper because the chr part is in lower case
                # Append half of the letter's ASCII value (integer division)
                half_value = letter_ascii // 2  # Divide by 2 and append
                converted_values.append(half_value)

    # Adjust the length of the list by appending duplicate values where necessary
    final_values = []
    for i in range(len(input_str)):
        final_values.append(converted_values[i % len(converted_values)])

    return final_values


def main() -> None:
    input_str: str = input('Enter the str : \n')

    final_values: list[int] = process_string(input_str.lower())
    
    print(final_values)
    print(sum(final_values))
    
    result_string = into_ascii_chr(final_values)
    print(f"\n{result_string}")
    
    return


if __name__ == "__main__":
    main()