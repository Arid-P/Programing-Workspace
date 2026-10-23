"""
Program 11: Number Classification (Armstrong, Perfect, Palindrome)
CBSE Class 11 Practical File

Objective:
Given an integer n, determine:
1. Is it an Armstrong number? (Sum of each digit raised to power of total digit count equals n)
   e.g., 153 = 1^3 + 5^3 + 3^3 = 153; 9474 = 9^4 + 4^4 + 7^4 + 4^4 = 9474.
2. Is it a Perfect number? (Sum of all proper positive divisors equals n)
   e.g., 6 = 1 + 2 + 3; 28 = 1 + 2 + 4 + 7 + 14.
3. Is it a Palindrome number? (Digits read same backwards and forwards, computed mathematically)
   e.g., 121, 1331, 12321.
"""

# I am only accepting positive integers


def is_armstrong(n: int) -> bool:
    """
    Check if positive integer n is an Armstrong number.
    Note: Standard Armstrong numbers are non-negative.
    """
    if n <= 0:
        return False

    k = len(str(n))
    dup_n: int = n
    cube_sum = 0

    while n > 0:
        last_digit: int = n % 10
        cube_sum += last_digit**k
        n //= 10

    if cube_sum != dup_n:
        return False

    return True


def is_perfect(n: int) -> bool:
    """
    Check if positive integer n is a Perfect number.
    A perfect number is equal to the sum of its proper positive divisors (excluding n itself).
    """
    if n <= 1:
        return False

    div_sum = 1
    for d in range(2, n):
        if n % d == 0:
            div_sum += d

    if div_sum != n:
        return False

    return True


def is_palindrome_number(n: int) -> bool:
    """
    Check if integer n is a palindrome number using arithmetic digit reversal
    (without converting the integer to a string).
    """
    if n < 0:
        return False

    reversed_num = 0
    temp = n
    while temp > 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp //= 10

    return reversed_num == n


if __name__ == "__main__":
    print("--- Program 11: Number Classification ---")
    num = int(input("Enter an integer to inspect: "))

    arm = is_armstrong(num)
    perf = is_perfect(num)
    pal = is_palindrome_number(num)

    print(f"\nResults for {num}:")
    print(f"- Armstrong Number:  {arm}")
    print(f"- Perfect Number:    {perf}")
    print(f"- Palindrome Number: {pal}")
