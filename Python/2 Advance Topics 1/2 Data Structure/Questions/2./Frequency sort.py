from collections import Counter as cnt

def main () -> None :
    #raise ValueError('main not implemented')
    text = "tree"

    counts = cnt(text)
    counts = dict((sorted(counts.items(), key=lambda k_v: -k_v[1])))
    """
    result = []
    for key, val in counts.items() :
        for i in range(val):
            result.append(key)
    """

    result = ''.join(key * val for key, val in counts.items())

    print(f"result = {''.join(result)}")
    return

if __name__ == "__main__" :
    main()


"""
GPT's unicode

from collections import Counter

def main() -> None:
    text = "tree"

    # Step 1: Count the frequency of each character
    counts = Counter(text)

    # Step 2: Create a list of empty lists to group characters by frequency
    max_freq = max(counts.values())  # Find the maximum frequency
    bucket = [[] for _ in range(max_freq + 1)]  # Create a list of empty lists
    
    # Step 3: Group characters by frequency
    for char, freq in counts.items():
        bucket[freq].append(char)

    # Step 4: Rebuild the result in the order of decreasing frequency
    result = []
    for freq in range(max_freq, 0, -1):  # Traverse from highest frequency to 1
        for char in bucket[freq]:
            result.append(char * freq)

    # Print the result as a string
    print(f"result = {''.join(result)}")
    return

if __name__ == "__main__":
    main()
"""