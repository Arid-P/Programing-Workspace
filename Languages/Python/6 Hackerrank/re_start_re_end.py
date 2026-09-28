# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

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



def find_substring_positions(s: str, k: str) -> list[tuple[int, int]]:
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
    s: str = input()
    k: str = input()
    
    
    answer_indexs: list[tuple[int, int]] = find_indexs(s, k)
    
    for idxs in answer_indexs :
        print(idxs)
    
    
    return

if __name__ == "__main__" :
    main()
