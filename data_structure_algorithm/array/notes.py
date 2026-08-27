
# ============================================
# 📌 TOPIC: Arrays
# ============================================

# 1. CORE IDEA
# A contiguous block of memory storing elements of the same type.
# Access any element instantly via index. Fixed size in most languages.
# Python's list is a dynamic array under the hood.

# 2. SYNTAX / STRUCTURE
# Python (dynamic array / list):
arr = [1, 2, 3, 4, 5]
arr[0]        # access
arr.append(6) # add to end
arr.pop()     # remove from end
arr.insert(2, 99)  # insert at index
arr.pop(2)    # remove at index

# 3. WORKING / MENTAL MODEL
# Think of memory as a row of numbered boxes.
# arr[0] is box 0, arr[1] is box 1, etc.
# Index access = jump directly to box N. O(1).
# Insert/delete in the middle = shift everything after it. O(n).
# Append to end = O(1) amortized (dynamic arrays occasionally resize).

# 4. EXAMPLES

# Basic — access and iteration
arr = [10, 20, 30, 40, 50]
print(arr[2])        # 30 — direct index jump, O(1)
for x in arr:        # O(n) — touching every element once
    print(x)

# Intermediate — find max without built-in
arr = [3, 7, 1, 9, 4]
max_val = arr[0]     # assume first is biggest
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]   # update when you find something bigger
print(max_val)       # 9

# Intermediate — reverse in-place using two pointers
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]  # swap
    left += 1
    right -= 1
# arr is now [5, 4, 3, 2, 1]
# no extra memory used — O(n) time, O(1) space

# 5. EDGE CASES / PITFALLS

# ❌ Off-by-one — last valid index is len-1, not len
arr = [1, 2, 3]
# arr[3]  → IndexError. Don't do this.

# ✅ Always use len(arr) - 1 for last element
print(arr[len(arr) - 1])  # 3
print(arr[-1])             # also 3 — Python shortcut

# ❌ Confusing append (end) with insert (anywhere)
arr.append(99)      # always O(1) amortized
arr.insert(0, 99)   # O(n) — shifts everything right

# ❌ Modifying a list while iterating over it
arr = [1, 2, 3, 4]
for x in arr:
    if x == 2:
        arr.remove(x)  # skips elements — undefined behaviour
# ✅ Iterate over a copy, or build a new list
arr = [x for x in arr if x != 2]

# 6. COMPARISONS
# Array vs Linked List:
# Array  → O(1) access, O(n) insert/delete middle
# Linked List → O(n) access, O(1) insert/delete if pointer in hand

# Static Array vs Dynamic Array (Python list):
# Static  → fixed size, no resize
# Dynamic → resizes when full (copies to bigger block), O(1) amortized append

# 7. SELF-TEST QUESTIONS
# - What is the time complexity of accessing arr[i]? Why?
# - Why is inserting at index 0 O(n)?
# - What does "amortized O(1)" mean for append?
# - What happens in memory when a dynamic array resizes?
# - Why is modifying a list during iteration dangerous?
# - What's the difference between pop() and pop(i)?

# 8. PRACTICE PROBLEMS
# Easy:
# - Return the second largest element in an array (no sorting).
# - Check if an array is a palindrome.
# - Count how many times a target value appears in an array.

# Medium:
# - Rotate an array to the right by k steps (in-place, no slicing).
# - Given a sorted array, remove duplicates in-place and return new length.
# - Find all pairs in an array that sum to a target value.

# Hard:
# - Given an array of integers, return indices of the two numbers
#   that add up to a target (no brute force O(n²) — use a hash map).
# - Given an unsorted array, find the length of the longest
#   consecutive sequence. O(n) only.

# 9. CONNECTIONS
# - Big-O you already know: access O(1), search O(n), insert O(n)
# - Loops you've written iterate arrays — same mental model
# - List comprehensions = concise array transformations
# - Hash Tables (coming up) are built on top of arrays internally

# 10. BUILD COMPONENT
# Build a function called running_average(arr) that takes a list of
# numbers and returns a new list where each element is the average
# of all elements up to and including that index.
# Example: [1, 3, 5, 7] → [1.0, 2.0, 3.0, 4.0]
# Constraints: one pass, no importing anything.