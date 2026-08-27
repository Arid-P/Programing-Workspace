"""
# itertools Module in Python

The `itertools` module provides a set of fast, memory-efficient tools for working with iterators. 
It includes functions for:
- Infinite iterators
- Combinatorial iterators
- Utility iterators

Let's explore them one by one with examples.
"""

import itertools

# 1️⃣ **Infinite Iterators** (cycle, count, repeat)
# These generate infinite sequences and must be used with caution.

print("🔹 Infinite Iterators")

# `count(start, step)`: Generates numbers indefinitely from 'start' with 'step'
print("count(10, 2):", list(itertools.islice(itertools.count(10, 2), 5)))  # [10, 12, 14, 16, 18]

# `cycle(iterable)`: Repeats elements of an iterable indefinitely
cycled = itertools.cycle(['A', 'B', 'C'])
print("cycle(['A', 'B', 'C']):", [next(cycled) for _ in range(6)])  # ['A', 'B', 'C', 'A', 'B', 'C']

# `repeat(value, times)`: Repeats a value a specified number of times
print("repeat('Hello', 3):", list(itertools.repeat('Hello', 3)))  # ['Hello', 'Hello', 'Hello']


# 2️⃣ **Combinatorial Iterators** (permutations, combinations, product, combinations_with_replacement)
# Useful for combinatorics and probability problems.

print("\n🔹 Combinatorial Iterators")

# `permutations(iterable, r)`: Returns all possible orderings of 'r' elements
print("permutations('ABC', 2):", list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# `combinations(iterable, r)`: Returns all combinations of 'r' elements (order doesn't matter)
print("combinations('ABC', 2):", list(itertools.combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# `product(iter1, iter2, ...)`: Cartesian product of given iterables
print("product('AB', '12'):", list(itertools.product('AB', '12')))
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# `combinations_with_replacement(iterable, r)`: Like combinations, but allows repeated elements
print("combinations_with_replacement('AB', 2):", list(itertools.combinations_with_replacement('AB', 2)))
# [('A', 'A'), ('A', 'B'), ('B', 'B')]


# 3️⃣ **Utility Iterators** (chain, islice, compress, groupby)
# These help in processing multiple iterables efficiently.

print("\n🔹 Utility Iterators")

# `chain(iter1, iter2, ...)`: Concatenates multiple iterables
print("chain('ABC', 'DEF'):", list(itertools.chain('ABC', 'DEF')))  # ['A', 'B', 'C', 'D', 'E', 'F']

# `islice(iterable, start, stop, step)`: Like slicing but for iterators
print("islice(range(10), 2, 8, 2):", list(itertools.islice(range(10), 2, 8, 2)))  # [2, 4, 6]

# `compress(iterable, selectors)`: Filters elements based on a corresponding list of booleans
print("compress('ABCDE', [1, 0, 1, 0, 1]):", list(itertools.compress('ABCDE', [1, 0, 1, 0, 1])))
# ['A', 'C', 'E']

# `groupby(iterable, key)`: Groups consecutive elements based on a key function
data = 'AAABBBCCCAAA'
grouped = [(key, list(group)) for key, group in itertools.groupby(data)]
print("groupby('AAABBBCCCAAA'):", grouped)
# [('A', ['A', 'A', 'A']), ('B', ['B', 'B', 'B']), ('C', ['C', 'C', 'C']), ('A', ['A', 'A', 'A'])]


"""
# Summary of `itertools` Functions

1. **Infinite Iterators**:
   - `count(start, step)`: Infinite counting
   - `cycle(iterable)`: Repeats items in a cycle
   - `repeat(value, times)`: Repeats a value 'n' times

2. **Combinatorial Iterators**:
   - `permutations(iterable, r)`: All possible orderings of 'r' elements
   - `combinations(iterable, r)`: All combinations of 'r' elements (order doesn't matter)
   - `product(iter1, iter2, ...)`: Cartesian product of iterables
   - `combinations_with_replacement(iterable, r)`: Like `combinations`, but allows repetitions

3. **Utility Iterators**:
   - `chain(iter1, iter2, ...)`: Concatenates multiple iterables
   - `islice(iterable, start, stop, step)`: Slices an iterable
   - `compress(iterable, selectors)`: Filters elements based on selectors
   - `groupby(iterable, key)`: Groups consecutive elements based on a key function
"""

# 🏁 End of itertools tutorial