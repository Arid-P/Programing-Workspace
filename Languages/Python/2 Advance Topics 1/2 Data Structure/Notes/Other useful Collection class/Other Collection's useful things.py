from collections import defaultdict
from collections import Counter
from collections import OrderedDict




# defaultdict

# Creating a defaultdict with a default value of 0
dd_int = defaultdict(int)  # Default is 0 for int
dd_int['apple'] = 1
dd_int['banana'] += 2

print(dd_int)  # Outputs: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})

# Using defaultdict with other default values
dd_int_list = defaultdict(list)  # Default is an empty list
dd_int_list['fruits'] = ['apple']
dd_int_list['seeds'].append('seasame')

print(dd_int_list)  # Outputs: defaultdict(<class 'list'>, {'fruits': ['apple'], 'seeds': ['seasame']})





#counter

# Creating a Counter
c = Counter("mississippi")
print(c)  # Outputs: Counter({'s': 4, 'i': 4, 'p': 2, 'm': 1})

# Most common elements
print(c.most_common(2))  # Outputs the 2 most common elements: [('s', 4), ('i', 4)]

# Updating counts
c.update("apple")
print(c)  # Outputs updated Counter





#orderedict
#now it is used for its method its main func of preserving the order or keys is present in py 3.7 above 

# Creating an OrderedDict
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Displaying the original OrderedDict
print("Original OrderedDict:", ordered_dict)

# Moving a key to the end
ordered_dict.move_to_end('a')
print("\nAfter moving 'a' to the end:", ordered_dict)

# Moving a key to the beginning (last=False)
ordered_dict.move_to_end('b', last=False)
print("\nAfter moving 'b' to the beginning:", ordered_dict)

# Popping the last item (default: last=True)
last_item = ordered_dict.popitem()
print("\nPopped last item:", last_item)
print("OrderedDict after popping last item:", ordered_dict)

# Popping the first item (last=False)
first_item = ordered_dict.popitem(last=False)
print("\nPopped first item:", first_item)
print("OrderedDict after popping first item:", ordered_dict)