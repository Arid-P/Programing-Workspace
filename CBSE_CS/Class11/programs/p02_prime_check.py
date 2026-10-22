"""
Program 02: Prime vs Composite Number Verification
CBSE Class 11 Practical File

Objective:
Input a positive integer n > 1 and determine whether it is prime or composite
using a for-loop with the else: suite and break.
"""

from math import sqrt

def is_prime(n: int) -> bool:
    for d in range(2, (int(sqrt(n)) + 1)):
        if n % d == 0:
            return False

    return True


if __name__ == "__main__":
    number = int(input("Enter an integer greater than 1: "))
    
    if number <= 1:
        print("Neither prime nor composite.")
    else:
        if is_prime(number):
            print(f"{number} is a PRIME number.")
        else:
            print(f"{number} is a COMPOSITE number.")

