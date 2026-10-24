# Notes on defaultdict from collections module

# What is defaultdict?
# - defaultdict is a subclass of the built-in dict class.
# - It allows you to set a default value for keys that don't exist yet.
# - This avoids KeyErrors when accessing missing keys.

# Why use defaultdict?
# - In regular dictionaries, trying to access a missing key results in a KeyError.
# - defaultdict automatically creates a default value for missing keys using a factory function.
# - Useful for collections like counting occurrences, grouping elements, etc.



# Basic Syntax
# You can initialize a defaultdict with a default factory function, which determines 
# the default value for missing keys.


from collections import defaultdict

# Initialize defaultdict with a default value factory
d = defaultdict(int)  # Default is 0 for every key
print(d["apple"])  # Output: 0 (default value)



# Example 1: Counting Occurrences of Words
def count_words(paragraph: str) -> defaultdict:
    """
    Counts the occurrences of words in a given paragraph using defaultdict.
    
    Args:
        paragraph (str): The paragraph containing words to be counted.
        
    Returns:
        defaultdict: A defaultdict with word counts.
    """
    word_count = defaultdict(int)  # Default is 0 for every word
    words = paragraph.split()  # Split the paragraph into words
    
    for word in words:
        word_count[word] += 1  # Increment count for each word
    
    return word_count

# Test count_words function
paragraph = "apple banana apple orange banana apple grape orange orange"
result = count_words(paragraph)
print(result)  # Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 3, 'grape': 1})



# Advantages of defaultdict:
# - No need for explicit checks to see if a key exists.
# - Automatically creates missing keys with default values.
# - Makes the code more concise and clean, especially in scenarios involving counting or grouping.


# Time Complexity:
# - Lookup: O(1)
# - Insertion: O(1) (amortized)
# - Default Value Creation: O(1) (amortized)