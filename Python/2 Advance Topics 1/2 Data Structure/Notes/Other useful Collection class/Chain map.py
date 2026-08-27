# ChainMap in Python (from collections module)
# A ChainMap is a class that groups multiple dictionaries into a single view.

# What is a ChainMap?
# - A ChainMap allows you to manage multiple dictionaries as a single unit.
# - It doesn't merge dictionaries but provides a unified view for key lookups.
# - ChainMap can be used to access keys across multiple dictionaries in the order provided.

# Use Case:
# - Useful when you have multiple sources of data (like different configuration files)
#   and you want to access them together without merging them.

from collections import ChainMap

# Creating dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

# Creating a ChainMap from multiple dictionaries
chain_map = ChainMap(dict1, dict2, dict3)

# Accessing values:
# It searches for the key in the order the dictionaries were passed
print(chain_map['a'])  # Output: 1 (from dict1)
print(chain_map['b'])  # Output: 2 (from dict1, first match found)
print(chain_map['c'])  # Output: 4 (from dict2, first match found)
print(chain_map['d'])  # Output: 5 (from dict3)

# Adding new mappings:
chain_map['e'] = 6
print(chain_map['e'])  # Output: 6 (added directly to the ChainMap)

# Removing a dictionary from the ChainMap
chain_map.maps.remove(dict3)
print(chain_map)  # ChainMap now contains dict1 and dict2 only

# Note: ChainMap is a view, so it doesn't modify the original dictionaries
print(dict1)  # dict1 remains unchanged
print(dict2)  # dict2 remains unchanged

# Advantages of ChainMap:
# 1. Multiple dictionaries can be accessed as one without merging them.
# 2. It provides an efficient way to look up keys in a sequence of dictionaries.
# 3. Updates to the ChainMap reflect in the underlying dictionaries.

# Time Complexity:
# - Key Lookup: O(1) on average (since dictionaries use hashing)
# - Insertion and Deletion: O(1) (for adding/removing mappings from the ChainMap)