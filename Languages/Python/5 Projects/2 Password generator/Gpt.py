import string as str
import random

# Global variables
conditions: list = []  # [length, lowercase, uppercase, digits, symbols, number of passwords]
password: str = ""

def generate_password() -> None:
    """
    Generates a password based on user-defined conditions.
    This function collects characters as per requirements and then shuffles them
    for randomness.
    """
    global conditions, password
    password_chars = []
    
    # Add characters based on conditions
    if conditions[1]:  # Lowercase letters
        password_chars.extend(random.choices(str.ascii_lowercase, k=conditions[0] // 4))
    if conditions[2]:  # Uppercase letters
        password_chars.extend(random.choices(str.ascii_uppercase, k=conditions[0] // 4))
    if conditions[3]:  # Digits
        password_chars.extend(random.choices(str.digits, k=conditions[0] // 4))
    if conditions[4]:  # Symbols
        password_chars.extend(random.choices(str.punctuation, k=conditions[0] // 4))

    # If length requirements aren't met, add random characters
    while len(password_chars) < conditions[0]:
        password_chars.append(random.choice(str.ascii_letters + str.digits + str.punctuation))

    # Shuffle to ensure randomness
    random.shuffle(password_chars)
    password = ''.join(password_chars)

def add_input_bool_to_conditions(condition: str) -> None:
    """
    Adds a boolean to the conditions list based on user input.
    """
    conditions.append(True if condition.lower() == 'y' else False)

def Inputs() -> None:
    """
    Takes user input for password conditions and validates input.
    """
    global conditions
    
    # Password length input with validation
    while True:
        length_str = input("Enter the length of your password: ")
        try:
            length = int(length_str)
            if length < 0:
                print("Input a valid positive integer.")
                continue
        except ValueError:
            print("Input a valid integer.")
            continue
        conditions.append(length)
        break
    
    # Conditions for each character type
    condition_name = ["lowercase", "uppercase", "digits", "symbols"]
    for condition in condition_name:
        input_value = input(f"Do you want {condition} characters in the password? (y for yes): ").lower()
        add_input_bool_to_conditions(input_value)
    
    # Number of passwords to generate with validation
    while True:
        no_password_str = input("Enter number of passwords you want: ")
        try:
            no_password = int(no_password_str)
            if no_password < 0:
                print("Input a valid positive integer.")
                continue
        except ValueError:
            print("Input a valid positive integer.")
            continue
        conditions.append(no_password)
        break

def main() -> None:
    """
    Main function to handle the generation and display of passwords.
    """
    Inputs()
    global password, conditions
    for i in range(1, conditions[5] + 1):
        generate_password()
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()