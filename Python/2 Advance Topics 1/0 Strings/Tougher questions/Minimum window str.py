from collections import Counter

def min_window_substring(s: str, t: str) -> str:
    """
    Finds the smallest substring of s that contains all characters in t.

    Args:
        s (str): The string to search in.
        t (str): The string containing characters to match.

    Returns:
        str: The smallest substring containing all characters in t, or an empty string if no such substring exists.
    """
    # Edge case: If either string is empty, return an empty result
    if not t or not s:
        return ""

    # Frequency map of characters in t
    t_freq = Counter(t)  # Counts occurrences of each character in t
    required = len(t_freq)  # Number of unique characters in t

    # Pointers for the sliding window
    left, right = 0, 0

    # Tracking variables
    formed = 0  # Number of unique characters in the window matching t's frequency
    window_counts = {}  # Frequency map of the current window
    min_len = float("inf")  # Minimum length of valid substring found
    min_window = ""  # Resultant smallest substring

    # Expand the window by moving the `right` pointer
    while right < len(s):
        char = s[right]  # Current character at the `right` pointer
        # Add it to the frequency map of the current window
        window_counts[char] = window_counts.get(char, 0) + 1
        
        print(f"{char=},    \n{window_counts=}\n\n")
        # Check if this character is in t and its count matches in the current window
        if char in t_freq and window_counts[char] == t_freq[char]:
            formed += 1
            print(f"{formed=},    \n\n")

        # Contract the window from the `left` if all characters in t are matched
        while left <= right and formed == required:
            char = s[left]  # Current character at the `left` pointer

            # Update the smallest valid window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]
                print(f"{min_window}")

            # Shrink the window by removing the character at `left`
            window_counts[char] -= 1
            if char in t_freq and window_counts[char] < t_freq[char]:
                formed -= 1
            print(f"inner  {char=},    \n{formed=},    \n{window_counts=}\n\n")

            # Move the `left` pointer to the right
            left += 1

        # Move the `right` pointer to expand the window
        right += 1

    # Return the smallest window found, or an empty string if no valid window exists
    return min_window

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(s)
print(t)
print((min_window_substring(s, t)))  # Output: "BANC"