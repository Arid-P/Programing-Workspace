"""
Program 15: Count Frequency of Elements in a List
CBSE Class 11 Practical File

Objective:
Given a list of elements, determine the frequency of occurrence of each unique element.
Implement two approaches:
1. Manual counting using traversal and a visited list (without using .count() or dictionaries).
2. Dictionary-based counting using standard key-value accumulation.
"""

from typing import Any


def count_frequencies_manual(lst: list) -> list[tuple[Any, int]]:
    """
    Count frequencies manually without built-in count() or dictionaries.

    Parameters:
        lst (list): List of arbitrary elements.

    Returns:
        list[tuple[Any, int]]: List of (element, frequency) tuples in order of first appearance.
    """
    unique = []
    for el in lst:
        if el not in unique:
            unique.append(el)

    frequency: list[tuple[Any, int]] = []

    for u_el in unique:
        freq = 0
        for el in lst:
            if el == u_el:
                freq += 1

        frequency.append((u_el, freq))

    return frequency


def count_frequencies_dict(lst: list) -> dict[Any, int]:
    """
    Count frequencies using a Python dictionary.

    Parameters:
        lst (list): List of hashable elements.

    Returns:
        dict[Any, int]: Mapping of element -> count.
    """
    unique = []
    for el in lst:
        if el not in unique:
            unique.append(el)

    frequency: dict[Any, int] = dict().fromkeys(unique, 0)
    del unique  # to free up space

    for u_el in frequency.keys():
        freq = 0
        for el in lst:
            if el == u_el:
                freq += 1

        frequency.update({u_el: freq})

    return frequency


if __name__ == "__main__":
    print("--- Program 15: Frequency of Elements in List ---")
    raw = input("Enter elements separated by spaces: ")
    elements = raw.split()

    print(f"\nOriginal List: {elements}")

    # Method 1: Manual List Frequency
    manual_freq = count_frequencies_manual(elements)
    print("\n--- Frequency Table (Manual Method) ---")
    print(f"{'Element':<15} {'Frequency':<10}")
    print("-" * 25)
    for item, count in manual_freq:
        print(f"{str(item):<15} {count:<10}")

    # Method 2: Dictionary Frequency
    dict_freq = count_frequencies_dict(elements)
    print("\n--- Frequency Table (Dictionary Method) ---")
    print(f"{'Element':<15} {'Frequency':<10}")
    print("-" * 25)
    for item, count in dict_freq.items():
        print(f"{str(item):<15} {count:<10}")
