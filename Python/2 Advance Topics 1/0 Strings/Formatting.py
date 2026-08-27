### 3. String Formatting

#### 3.1. F-strings
# - **F-strings**: Introduced in Python 3.6, they allow for easy embedding of expressions 
#   inside string literals using curly braces `{}`.
# - **Expression Evaluation**: You can include any valid Python expression inside the braces.

name = "Aridaman"
age = 15
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Aridaman and I am 15 years old.

# Including expressions
area = 5 * 3
message = f"The area of the rectangle is {area} square units."
print(message)  # Output: The area of the rectangle is 15 square units



#---------------------------------------------------------------------



#### 3.2. `.format()`
# - **`str.format()`**: Allows more complex formatting options, where placeholders 
#   in the string are replaced with values.
# - **Positional and Keyword Arguments**: You can specify the order of the arguments.

name = "Aridaman"
age = 15
greeting = "Hello, my name is {} and I am {} years old.".format(name, age)
print(greeting)  # Output: Hello, my name is Aridaman and I am 15 years old.

# Using positional arguments
greeting = "Hello, my name is {0} and I am {1} years old. {0} likes programming.".format(name, age)
print(greeting)  # Output: Hello, my name is Aridaman and I am 15 years old. Aridaman likes programming.

# Using keyword arguments
greeting = "Hello, my name is {name} and I am {age} years old.".format(name=name, age=age)
print(greeting)  # Output: Hello, my name is Aridaman and I am 15 years old.

# Advanced Formatting: You can format numbers, dates, and more.
number = 1234.56789
formatted_number = "The formatted number is {:.2f}".format(number)
print(formatted_number)  # Output: The formatted number is 1234.57



#---------------------------------------------------------------------



#### 3.3. `%` Formatting
# - **Percent Formatting**: An older method that uses the `%` operator for string interpolation.

name = "Aridaman"
age = 15
greeting = "Hello, my name is %s and I am %d years old." % (name, age)
print(greeting)  # Output: Hello, my name is Aridaman and I am 15 years old.

# Formatting multiple values
height = 5.8
greeting = "Hello, my name is %s, I am %d years old, and my height is %.1f feet." % (name, age, height)
print(greeting)  # Output: Hello, my name is Aridaman, I am 15 years old, and my height is 5.8 feet.

# Additional Formatting: You can specify width and precision.
number = 42.123456
formatted = "Formatted number: %.2f" % number
print(formatted)  # Output: Formatted number: 42.12



#---------------------------------------------------------------------



#### 3.4. Comparison of Methods
# - **F-strings**: Most modern and flexible, allows expression evaluation and is easy to read.
# - **`str.format()`**: More versatile than `%` formatting, supports advanced formatting options 
#   but less concise than f-strings.
# - **`%` Formatting**: Older style, still widely used, but can be less readable and more error-prone for complex formats.