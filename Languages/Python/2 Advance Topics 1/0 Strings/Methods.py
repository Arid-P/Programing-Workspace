# ### 2. String Methods

# #### 2.1. `lower()` and `upper()`
# - **`str.lower()`**: Converts all characters in the string to lowercase.
# - **`str.upper()`**: Converts all characters in the string to uppercase.

text = "Hello, World!"
print(text.lower())  # Output: hello, world!
print(text.upper())  # Output: HELLO, WORLD!



# ---------------  



# #### 2.2. `strip()`
# - **`str.strip()`**: Removes any leading and trailing whitespace (spaces, tabs, newlines) from the string.
# Can also remove specific characters if provided as arguments.

text = "   Hello, World!   "
cleaned_text = text.strip()
print(f"Original: '{text}'")  # Output: '   Hello, World!   '
print(f"Cleaned: '{cleaned_text}'")  # Output: 'Hello, World!'


# Additional Examples:

# - **Removing Specific Characters:**
text = "---Hello, World!---"
cleaned_text = text.strip('-')
print(f"Original: '{text}'")  # Output: '---Hello, World!---'
print(f"Cleaned: '{cleaned_text}'")  # Output: 'Hello, World!'


# - **Leading Whitespace Only:**
text = "   Hello, World!"
leading_cleaned_text = text.lstrip()
print(f"Original: '{text}'")  # Output: '   Hello, World!'
print(f"Leading Cleaned: '{leading_cleaned_text}'")  # Output: 'Hello, World!'


# - **Trailing Whitespace Only:**
text = "Hello, World!   "
trailing_cleaned_text = text.rstrip()
print(f"Original: '{text}'")  # Output: 'Hello, World!   '
print(f"Trailing Cleaned: '{trailing_cleaned_text}'")  # Output: 'Hello, World!'


# - **Combining Methods:**
text = "   Python   "
cleaned_text = text.strip().upper()
print(f"Cleaned and Uppercased: '{cleaned_text}'")  # Output: 'PYTHON'



# ---------------  



# #### 2.3. `split()`

# - **`str.split(separator)`**: Splits the string into a list based on the specified separator.
# If no separator is provided, it splits at whitespace.


text = "Hello, World!"
words = text.split(", ")
print(words)  # Output: ['Hello', 'World!']



# ---------------  



# #### 2.4. `join()`

# - **`separator.join(iterable)`**: Joins elements of an iterable (like a list) into a single string,
# with the specified separator between each element.

words = ['Hell', 'World']
joined_text = ", ".join(words)
print(joined_text)  # Output: Hello, World



#---------------  



# #### 2.5. `title()`

# - **`str.title()`**: Capitalizes the first letter of each word in the string.

text = "hello, world!"
print(text.title())  # Output: Hello, World!



# ---------------  


# #### 2.6. `isdigit()`, `isalpha()`, `isalnum()`, etc.

# - **`str.isdigit()`**: Returns `True` if all characters in the string are digits.

# - **`str.isalpha()`**: Returns `True` if all characters in the string are alphabetic.

# - **`str.isalnum()`**: Returns `True` if all characters in the string are only alphanumeric (letters or numbers).

text1 = "12345"
text2 = "Hello"
text3 = "hello123"

print(text1.isdigit())  # Output: True
print(text2.isalpha())  # Output: True
print(text3.isalnum())  # Output: True