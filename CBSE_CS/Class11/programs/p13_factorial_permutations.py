"""
Program 13: Factorial, Permutations (nPr), and Combinations (nCr)
CBSE Class 11 Practical File

Objective:
1. Compute the factorial of a non-negative integer n using an iterative loop (n! = 1 * 2 * ... * n).
2. Compute Permutations: nPr = n! / (n - r)!
3. Compute Combinations: nCr = n! / (r! * (n - r)!)
"""


def compute_factorial(n: int) -> int:
    """
    Calculate n! iteratively.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n (0! = 1, 1! = 1).
        Raises ValueError if n < 0.
    """

    if n < 0:
        raise ValueError("only non negative integers are within the domain")
    elif n == 0:
        return 1

    fact = 1
    while n > 0:
        fact *= n
        n = n - 1

    return fact


def compute_nPr(n: int, r: int) -> int:
    """
    Compute permutations: n! / (n - r)!
    Valid conditions: 0 <= r <= n
    """
    if n < r:
        raise ValueError(
            "n (number of objects) must be greater or equal to r (number of objects being selected)"
        )
    elif n == r:
        return compute_factorial(n)
    elif n < 0 or r < 0:
        raise ValueError("Only non negaative integers are in domain")

    return compute_factorial(n) // compute_factorial(n - r)  


def compute_nCr(n: int, r: int) -> int:
    """
    Compute combinations: n! / (r! * (n - r)!)
    Valid conditions: 0 <= r <= n
    """
    if n == r:
        return 1

    return compute_nPr(n, r) // compute_factorial(r)  


if __name__ == "__main__":
    print("--- Program 13: Factorial, nPr, and nCr ---")
    n_val = int(input("Enter n (total items >= 0): "))
    r_val = int(input("Enter r (items chosen, 0 <= r <= n): "))

    if n_val < 0 or r_val < 0 or r_val > n_val:
        print("Invalid inputs! Ensure n >= 0 and 0 <= r <= n.")
    else:
        fact_n = compute_factorial(n_val)
        fact_r = compute_factorial(r_val)
        npr = compute_nPr(n_val, r_val)
        ncr = compute_nCr(n_val, r_val)

        print(f"\nFactorial ({n_val}!): {fact_n}")
        print(f"Factorial ({r_val}!): {fact_r}")
        print(f"Permutations P({n_val}, {r_val}): {npr}")
        print(f"Combinations C({n_val}, {r_val}): {ncr}")
