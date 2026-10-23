"""
Program 09: Fibonacci Series Generation
CBSE Class 11 Practical File

Objective:
1. Generate and return the first N terms of the Fibonacci sequence:
   0, 1, 1, 2, 3, 5, 8, 13, 21, ...
2. Generate all Fibonacci numbers less than or equal to a specified upper limit M.
"""

from typing import Optional


def generate_fibonacci_n_terms(n: int) -> list[int]:
    """
    Generate the first n terms of the Fibonacci series.

    Parameters:
        n (int): Number of terms to generate.

    Returns:
        list[int]: A list containing the first n Fibonacci numbers.
                   If n <= 0, return an empty list [].
    """

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = [0] * n  # to save from the new memory chunk hazard with append
        series[1] = 1

    for i in range(2, n):
        series[i] = series[i - 1] + series[i - 2]

    return series


def generate_fibonacci_up_to_limit(limit: int) -> list[int]:
    """
    Generate all Fibonacci numbers less than or equal to `limit`.

    Parameters:
        limit (int): Upper bound value.

    Returns:
        list[int]: All Fibonacci numbers <= limit.
                   If limit < 0, return [].
    """
    if limit < 0:
        return []
    elif limit == 0:
        return [0]
    elif limit == 1:
        return [0, 1, 1]

    series = [0, 1, 1]

    i = 3
    while True:
        curr_term = series[i - 1] + series[i - 2]

        if curr_term > limit:
            return series

        series.append(curr_term)
        i += 1


if __name__ == "__main__":
    print("--- Program 09: Fibonacci Series ---")

    # 1. First N terms
    num_terms = int(input("Enter number of terms (N): "))
    terms = generate_fibonacci_n_terms(num_terms)
    print(f"First {num_terms} Fibonacci terms: {terms}")

    # 2. Terms up to limit
    max_val = int(input("\nEnter maximum value limit (M): "))
    series_limit = generate_fibonacci_up_to_limit(max_val)
    print(f"Fibonacci terms up to {max_val}: {series_limit}")
