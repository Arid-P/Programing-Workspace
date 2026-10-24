from sympy import symbols, Eq, solve
from functools import lru_cache

# Define the variable
x = symbols('x')

# Function to solve the equation with caching
@lru_cache(None)
def compute_solutions():
    # Given equation
    equation = Eq((x + 1) * (x**2 + 1) * (x**3 + 1), 30 * x**3)

    # Solve the equation
    solutions = solve(equation, x)
    return solutions

# Function to print solutions and their sum
def display_solutions():
    solutions = compute_solutions()

    # Separate real and complex solutions
    real_solutions = [sol.evalf() for sol in solutions if sol.is_real]
    complex_solutions = [sol.evalf() for sol in solutions if not sol.is_real]

    print("Solutions to the equation:")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}: {sol}")
        print(f"Solution {i}: {sol.evalf()}")

    print("\nReal solutions:")
    for sol in real_solutions:
        print(sol)

    print("\nComplex solutions:")
    for sol in complex_solutions:
        print(sol)

    # Calculate and print the sum of real solutions
    real_solutions_sum = sum(real_solutions)
    print(f"\nSum of real solutions: {real_solutions_sum}")

# Call the function to display solutions
display_solutions()