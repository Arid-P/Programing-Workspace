"""
Program 04: Count Vowels, Consonants, Uppercase, and Lowercase Characters
CBSE Class 11 Practical File

Objective:
Input a string from the user and count the total number of:
1. Vowels (A, E, I, O, U, case-insensitive)
2. Consonants (alphabetic letters that are not vowels)
3. Uppercase letters
4. Lowercase letters
"""


def analyze_string(text: str) -> dict[str, int]:
    counter = {"vowels": 0, "consonants": 0, "uppercase": 0, "lowercase": 0}

    for el in text:
        if not el.isalpha():
            continue

        #Checking for vowels and consonants
        if el.lower() in ["a", "e", "i", "o", "u"]:
            counter["vowels"] += 1
        else:
            counter["consonants"] += 1

        #Checking for uppercase and lowercase
        if el.islower():
            counter["lowercase"] += 1
        else:
            counter["uppercase"] += 1

    return counter


if __name__ == "__main__":
    line = input("Enter a string: ")
    counts = analyze_string(line)

    print("\n--- String Analysis ---")
    print(f"Vowels:     {counts.get('vowels', 0)}")
    print(f"Consonants: {counts.get('consonants', 0)}")
    print(f"Uppercase:  {counts.get('uppercase', 0)}")
    print(f"Lowercase:  {counts.get('lowercase', 0)}")
