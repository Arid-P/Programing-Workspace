# re_library_notes.py

"""
Python `re` Module - Regular Expressions
----------------------------------------
The `re` module in Python is used for pattern matching, searching, and string manipulation 
using **Regular Expressions (Regex)**.

Key Functions in `re`:
1. `re.match()`   - Matches the pattern at the **beginning** of the string.
2. `re.search()`  - Searches for the **first occurrence** of the pattern anywhere in the string.
3. `re.findall()` - Returns a **list** of all occurrences of the pattern.
4. `re.sub()`     - Replaces occurrences of a pattern with another string.
5. `re.split()`   - Splits a string based on a pattern.

"""

import re  # Importing the `re` module

# 1. re.match() - Matches the pattern only at the beginning of the string
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
print(match)  # Output: <re.Match object; span=(0, 5), match='hello'>

# 2. re.search() - Searches for the first occurrence of the pattern anywhere in the string
pattern = r"world"
search = re.search(pattern, text)
print(search)  # Output: <re.Match object; span=(6, 11), match='world'>

# 3. re.findall() - Returns a list of all occurrences of the pattern in the string
text = "apple, banana, apple, orange"
pattern = r"apple"
all_matches = re.findall(pattern, text)
print(all_matches)  # Output: ['apple', 'apple']

# 4. re.sub() - Replaces occurrences of a pattern with another string
text = "I love cats"
pattern = r"cats"
new_text = re.sub(pattern, "dogs", text)
print(new_text)  # Output: I love dogs

# 5. re.split() - Splits a string based on a pattern
text = "apple, banana; orange, grape"
pattern = r"[,;] "  # Splits on commas or semicolons followed by a space
split_text = re.split(pattern, text)
print(split_text)  # Output: ['apple', 'banana', 'orange', 'grape']

"""
Common Regular Expression Patterns
----------------------------------
| Pattern | Description | Example Match |
|---------|-------------|--------------|
| \d      | Matches a digit (0-9) | "1", "5" |
| \D      | Matches a non-digit | "A", "b", "@" |
| \w      | Matches a word character (letters, digits, underscore) | "abc", "123", "_word" |
| \W      | Matches a non-word character | "@", "!" |
| \s      | Matches whitespace (spaces, tabs, newlines) | " " |
| \S      | Matches a non-whitespace character | "A", "b" |
| ^       | Matches start of a string | ^hello (matches "hello world") |
| $       | Matches end of a string | world$ (matches "hello world") |
| .       | Matches any character except newline | "a", "1", "@" |
| *       | Matches 0 or more occurrences | "ca*t" matches "ct", "cat", "caaaat" |
| +       | Matches 1 or more occurrences | "ca+t" matches "cat", "caaaat" but not "ct" |
| ?       | Matches 0 or 1 occurrence | "colou?r" matches "color", "colour" |
| {n}     | Matches exactly `n` times | "a{3}" matches "aaa" |
| {n,}    | Matches `n` or more times | "a{2,}" matches "aa", "aaa", "aaaa" |
| {n,m}   | Matches between `n` and `m` times | "a{2,4}" matches "aa", "aaa", "aaaa" |
"""

# Example: Extracting Emails from a Text using Regex
text = "Contact us at support@example.com or sales@company.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)  # Output: ['support@example.com', 'sales@company.org']

"""
Key Takeaways:
--------------
- Regular expressions provide powerful pattern matching for strings.
- The `re` module functions allow us to search, replace, and extract data efficiently.
- Understanding regex syntax helps in validating and processing text data.

"""