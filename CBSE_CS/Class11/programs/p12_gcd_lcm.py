"""
Program 12: Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
CBSE Class 11 Practical File

Objective:
1. Compute the Greatest Common Divisor (GCD / HCF) of two integers using the Euclidean algorithm.
2. Compute the Least Common Multiple (LCM) of two integers using the relationship:
   LCM(a, b) = abs(a * b) // GCD(a, b)
"""


def compute_gcd(a: int, b: int) -> int:
    """
    Compute the GCD of two integers using the Euclidean algorithm.

    Parameters:
        a (int), b (int): Input integers.

    Returns:
        int: Greatest common divisor (non-negative).
    """

    if a <= 0 or b <= 0:
        raise ValueError("GCD of non positive numbers cannot be computed")
    elif a == 1 or b == 1:
        return 1

    while b > 0:
        a, b = b, a % b
    return a


def compute_lcm(a: int, b: int) -> int:
    """
    Compute the LCM of two integers.

    Parameters:
        a (int), b (int): Input integers.

    Returns:
        int: Least common multiple.
        Note: If either a or b is 0, LCM is defined as 0.
    """

    if a == 0 or b == 0:
        return 0
    elif a <= 0 or b <= 0:
        raise ValueError("LCM of negative numbers cannot be computed")
    
    gcd = compute_gcd(a, b)
    return a * b // gcd 


if __name__ == "__main__":
    print("--- Program 12: GCD & LCM Calculator ---")
    val_a = int(input("Enter first integer (a): "))
    val_b = int(input("Enter second integer (b): "))

    gcd_res = compute_gcd(val_a, val_b)
    lcm_res = compute_lcm(val_a, val_b)

    print(f"\nFor numbers {val_a} and {val_b}:")
    print(f"- GCD (HCF): {gcd_res}")
    print(f"- LCM:       {lcm_res}")
