def is_palindromic (chrs: list[str]) -> bool :
    reverse_chrs: list[str] = chrs.copy()
    reverse_chrs.reverse()
    return chrs == reverse_chrs


def longest_palindromic_substring(s: str) -> list[str]:
    right = len(s)
    palindroms: list[str]= []
    
    while right >= 1 :
        left = 0
        while left < right - 1 :
            subs = s[left : right]
            if is_palindromic(subs) :
                palindroms.append(''.join(subs))
            left += 1
        
        right -= 1
    
    palindroms = sorted(palindroms, key=lambda palindrom: len(palindrom))
    
    print(f"{palindroms=}")
    
    
    max_len = len(palindroms[-1])
    
    longest_palindroms = [str(palindroms[-1])]
    for index in range(-2, -len(palindroms)-1, -1) :
        if len(palindroms[index]) == max_len :
            longest_palindroms.append(str(palindroms[index]))
        else :
            break
    
    return longest_palindroms


def main () :
    s = "babad"
    s_list = list(s)
    print(f"{longest_palindromic_substring(s_list)=}")
    #print(is_palindromic(['b', 'b']))

if __name__ == "__main__" :
    main()