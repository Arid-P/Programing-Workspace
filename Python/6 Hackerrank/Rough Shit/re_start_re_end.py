# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import timeit
from typing import List, Tuple

import random
import string


def generate_large_input(size: int, pattern_size: int) -> Tuple[str, str]:
    """
    Generates a large random string and a random pattern.

    Args:
        size (int): Length of the main string `s`.
        pattern_size (int): Length of the substring `k`.

    Returns:
        Tuple[str, str]: A tuple containing the large string `s` and a substring `k` from `s`.
    """
    s = ''.join(random.choices(string.ascii_lowercase, k=size))  # Large random string
    start_idx = random.randint(0, size - pattern_size)  # Random index for substring
    k = s[start_idx:start_idx + pattern_size]  # Extract substring from `s`
    return s, k


# large_s, large_k = generate_large_input(10**6, 5)

def find_indexs (s: str, k: str) -> list[tuple[int, int]] :
    s_ptr: int = 0
    e_ptr: int = len(k)
    
    answer_indexs: list[tuple[int, int]] = []
    while e_ptr <= len(s) :
        if k == s[s_ptr:e_ptr] :
            answer_indexs.append( (s_ptr, e_ptr) )
        s_ptr += 1
        e_ptr += 1
    
    if not answer_indexs :
        answer_indexs.append( (-1, -1) )
    
    return answer_indexs



def find_substring_positions(s: str, k: str) -> List[Tuple[int, int]]:
    """
    Finds all occurrences of substring k in string s and returns their (start, end) indices.

    Args:
        s (str): The input string.
        k (str): The substring to find.

    Returns:
        List[Tuple[int, int]]: A list of (start, end) index pairs. If no match is found, returns [(-1, -1)].
    """
    matches = list(re.finditer(f'(?={k})', s))
    
    # If no match is found, return [(-1, -1)]
    if not matches:
        return [(-1, -1)]
    
    return [(match.start(), match.start() + len(k) - 1) for match in matches]



def main () -> None :
    # s: str = input()
#     k: str = input()
    
    s, k = generate_large_input(10**6, 5)
    
    # answer_indexs: list[tuple[int, int]] = find_indexs(s, k)
#     
#     for idxs in answer_indexs :
#         print(idxs)
    
    # Using lambda to pass arguments
    execution_time1 = timeit.timeit(lambda: find_indexs(s, k), number=100000)
    execution_time2 = timeit.timeit(lambda: find_substring_positions(s, k), number=100000)
    print(f"Execution time of find_indexs: {execution_time1:.6f} seconds")
    print(f"Execution time of find_substring_positions: {execution_time2:.6f} seconds")
    
    return

if __name__ == "__main__" :
    main()
