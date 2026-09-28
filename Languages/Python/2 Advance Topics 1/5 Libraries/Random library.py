# Notes for `random` Library
# This file contains explanations and code examples for working with the `random` library in Python.

# 1. Importing the `random` Library
# To use the `random` library, you need to import it first. You can also use an alias if needed.
import random as r

# 2. Generating Random Numbers
# a. Generating a random floating-point number in a range [0.0, 1.0)
# - r.random(): Returns a random floating-point number between 0 and 1 (inclusive of 0, exclusive of 1).

print(f"Random number between 0 and 1: {r.random()}")  # Generating a random float between 0 and 1

# b. Generating a random integer within a specified range
# - r.randint(a, b): Returns a random integer between a and b, inclusive.

print(f"Random integer between 1 and 10: {r.randint(1, 10)}")  # Generating a random integer between 1 and 10

# c. Generating a random floating-point number within a specified range
# - r.uniform(a, b): Returns a random floating-point number between a and b.

print(f"Random float between 1.5 and 5.5: {r.uniform(1.5, 5.5)}")  # Generating a random float between 1.5 and 5.5

# 3. Working with Sequences
# a. Choosing a random element from a sequence (e.g., list or tuple)
# - r.choice(seq): Returns a randomly selected element from the non-empty sequence `seq`.

items = ['apple', 'banana', 'cherry', 'date']
print(f"Random fruit from the list: {r.choice(items)}")  # Selecting a random item from a list

# b. Choosing multiple random elements (without replacement)
# - r.sample(seq, k): Returns a list of `k` unique elements chosen from the population sequence `seq`.

print(f"Random sample of 2 fruits from the list: {r.sample(items, 2)}")  # Random sample without replacement

# c. Shuffling elements of a sequence
# - r.shuffle(seq): Shuffles the elements of the sequence `seq` in place (does not return a new sequence).

print("Original list before shuffle:", items)
r.shuffle(items)  # Shuffling the list
print("List after shuffle:", items)  # List after shuffling

# 4. Working with Random Choices with Replacement
# a. Generating random elements with replacement
# - r.choices(seq, k): Returns a list of `k` elements selected from the sequence `seq` with replacement.

print(f"Random sample of 3 fruits (with replacement): {r.choices(items, k=3)}")  # Random sample with replacement

# 5. Randomly Setting a Seed for Reproducibility
# a. r.seed(): Initializes the random number generator. By using a seed, you can get the same random sequence every time.

r.seed(42)  # Set the seed to ensure reproducibility
print(f"Random number with seed 42: {r.random()}")  # Generates a reproducible random number

# 6. Generating Random Values Based on Probability Distributions
# a. r.gauss(mu, sigma): Generates a random value based on a Gaussian (normal) distribution with mean `mu` and standard deviation `sigma`.

print(f"Random number from Gaussian distribution with mean 0 and stddev 1: {r.gauss(0, 1)}")  # Gaussian distribution

# b. r.betavariate(alpha, beta): Generates a random value based on a Beta distribution.

print(f"Random number from Beta distribution with alpha=2 and beta=5: {r.betavariate(2, 5)}")  # Beta distribution

# 7. Other Useful Functions
# a. r.randrange(start, stop, step): Returns a randomly selected element from the range(start, stop, step).
# - Similar to `range()`, but the step value can also be specified.

print(f"Random number from range 0 to 10 with step 2: {r.randrange(0, 10, 2)}")  # Random number with step

# b. r.triangular(low, high, mode): Generates a random number based on a triangular distribution.

print(f"Random number from triangular distribution (low=0, high=10, mode=5): {r.triangular(0, 10, 5)}")  # Triangular distribution