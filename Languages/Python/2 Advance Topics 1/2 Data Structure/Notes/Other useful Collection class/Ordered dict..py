# Notes on OrderedDict from collections module

# What is OrderedDict?
# - OrderedDict is a subclass of the built-in dict class.
# - It maintains the insertion order of the keys, unlike regular dicts (in earlier Python versions).
# - Python 3.7+ guarantees order in dict, but OrderedDict still has extra functionalities.

# Syntax
from collections import OrderedDict

# Initialize an ordered dictionary
ordered_dict = OrderedDict([("apple", 1), ("banana", 2), ("orange", 3)])

# Example 1: Basic usage
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])

# Example 2: Using move_to_end() method
ordered_dict.move_to_end("banana")
print(ordered_dict)  # Output: OrderedDict([('apple', 1), ('orange', 3), ('banana', 2)])

ordered_dict.move_to_end("orange", last=False)
print(ordered_dict)  # Output: OrderedDict([('orange', 3), ('apple', 1), ('banana', 2)])

# Example 3: Using popitem() method
item = ordered_dict.popitem()
print(item)  # Output: ('banana', 2)

item = ordered_dict.popitem(last=False)
print(item)  # Output: ('orange', 3)

# Advantages of OrderedDict:
# - Preserves insertion order.
# - Supports reordering with methods like move_to_end().
# - Useful in scenarios where order matters.

# Time Complexity:
# - Insertion: O(1)
# - Lookup: O(1)
# - move_to_end(): O(1)
# - popitem(): O(1)