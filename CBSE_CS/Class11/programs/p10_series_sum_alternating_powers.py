"""
Program 10: Sum of Mathematical Series
CBSE Class 11 Practical File

Objective:
1. Compute the sum of the geometric power series:
   S1 = 1 + x + x^2 + x^3 + ... + x^n
2. Compute the sum of the alternating series with factorials:
   S2 = x - (x^2 / 2!) + (x^3 / 3!) - (x^4 / 4!) + ... + ((-1)^(n+1) * x^n / n!)
"""


def sum_geometric_powers(x: float, n: int) -> float:
    """
    Calculate the sum: 1 + x + x^2 + x^3 + ... + x^n

    Parameters:
        x (float): Base value.
        n (int): Maximum power (non-negative integer).

    Returns:
        float: Sum of the series.
    """
    total = 0.0
    for i in range(n + 1):
        total += x ** i
    return total


def sum_alternating_factorial_series(x: float, n: int) -> float:
    """
    Calculate the alternating series sum:
    x - (x^2 / 2!) + (x^3 / 3!) - (x^4 / 4!) + ... up to n terms.

    Parameters:
        x (float): Base value.
        n (int): Number of terms (n >= 1).

    Returns:
        float: Sum of the series.
    """
    # TODO: Implement accumulation loop for S2.
    from math import factorial as fact

    series = 0
    for i in range(1, n + 1):
        series += (-1) ** (i - 1) * (x**i / fact(i))

    return series


if __name__ == "__main__":
    print("--- Program 10: Mathematical Series Sums ---")
    val_x = float(input("Enter value of x: "))
    val_n = int(input("Enter value of n (integer >= 0): "))

    # 1. Geometric Powers
    s1 = sum_geometric_powers(val_x, val_n)
    print(f"\nSeries 1: 1 + x + x^2 + ... + x^{val_n} = {s1}")

    # 2. Alternating Factorial Series
    if val_n >= 1:
        s2 = sum_alternating_factorial_series(val_x, val_n)
        print(f"Series 2: x - x^2/2! + x^3/3! - ... ({val_n} terms) = {s2}")
    else:
        print("Series 2 requires n >= 1.")
