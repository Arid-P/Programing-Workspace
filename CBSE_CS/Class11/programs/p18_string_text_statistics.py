"""
Program 18: Text & String Analysis — Comprehensive Character & Word Statistics
CBSE Class 11 Practical File

Objective:
Given a passage of text (single or multi-line), compute and return detailed character metrics:
1. Line count
2. Word count
3. Total character count
4. Vowels and Consonants count
5. Digits count
6. Whitespace count (spaces, tabs, newlines)
7. Special characters / punctuation symbols count
"""


def analyze_text(text: str) -> dict[str, int]:
    """
    Analyze a string and compute comprehensive character and text statistics.

    Parameters:
        text (str): Input text string.

    Returns:
        dict[str, int]: A dictionary containing counts for:
            - "lines": Number of lines
            - "words": Number of whitespace-separated words
            - "characters": Total length of text
            - "vowels": English vowels (A, E, I, O, U, case-insensitive)
            - "consonants": English alphabetic characters that are not vowels
            - "digits": Numeric digits (0-9)
            - "whitespaces": Spaces, tabs, and newlines
            - "special_characters": Non-alphanumeric, non-whitespace characters
    """
    # whitespace dont count as chr
    stat: dict[str, int] = {
        "lines": len(text.splitlines()) if text else 0,
        "words": len(text.split()),
        "characters": len(text),
        "vowels": 0,
        "consonants": 0,
        "digits": 0,
        "whitespaces": 0,
        "special_characters": 0,
    }

    VOWELS = set("aeiouAEIOU")

    for c in text:
        if c in VOWELS:
            stat["vowels"] += 1
        elif c.isalpha():
            stat["consonants"] += 1
        elif c.isdigit():
            stat["digits"] += 1
        elif c.isspace():
            stat["whitespaces"] += 1
        else:
            stat["special_characters"] += 1

    return stat


if __name__ == "__main__":
    print("--- Program 18: Text & String Analysis ---")
    print("Enter your text below (Press Enter on an empty line to finish):")

    lines: list[str] = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    sample_text = "\n".join(lines)

    if not sample_text:
        print("\nNo text entered.")
    else:
        stats = analyze_text(sample_text)
        print("\n" + "=" * 40)
        print(f"{'Text Metric':<25} {'Count':<10}")
        print("=" * 40)
        for metric, count in stats.items():
            formatted_name = metric.replace("_", " ").title()
            print(f"{formatted_name:<25} {count:<10}")
        print("=" * 40)
