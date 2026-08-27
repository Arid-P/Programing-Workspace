# Notes on Counter from collections module

# What is Counter?
# - Counter is a subclass of dict designed for counting hashable elements.
# - It simplifies counting occurrences of elements in an iterable (e.g., list, string).

# Syntax
from collections import Counter

# Example 1: Counting occurrences
numbers = [1, 2, 2, 3, 3, 3, 4]
counter = Counter(numbers)
print(counter)  # Output: Counter({3: 3, 2: 2, 1: 1, 4: 1})

# Example 2: Using most_common() method
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(words)
most_common_elements = counter.most_common(2)
print(most_common_elements)  # Output: [('apple', 3), ('banana', 2)]

# Example 3: Operations with Counters
counter1 = Counter([1, 2, 2, 3])
counter2 = Counter([2, 3, 3, 4])
sum_counter = counter1 + counter2
print(sum_counter)  # Output: Counter({2: 3, 3: 3, 1: 1, 4: 1})

# Subtracting Counter objects
diff_counter = counter1 - counter2
print(diff_counter)  # Output: Counter({1: 1})

# Intersection of Counters
intersection_counter = counter1 & counter2
print(intersection_counter)  # Output: Counter({2: 1, 3: 1})

# Example 4: elements() Method
elements = list(counter.elements())
print(elements)  # Output: [1, 2, 2, 3, 3, 3]

# Advantages of Counter:
# - Efficient counting and tracking of occurrences.
# - Supports arithmetic operations and other methods like most_common() and elements().
# - Useful for various applications like frequency analysis and inventory management.

# Time Complexity:
# - Counting: O(n), where n is the number of elements in the iterable.
# - Accessing count: O(1).
# - most_common(): O(n log k), where n is the number of elements and k is the number of most common elements requested.