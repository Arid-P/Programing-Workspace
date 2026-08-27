
def len_long_substr (s: str) -> int :
    longest_sub: str = ""
    
    idx = 1
    for chr1 in s :
        curr_sub: str = chr1
        
        for chr2 in s[idx : ] :
            if chr2 not in curr_sub :
                curr_sub += chr2
            elif len(curr_sub) > len(longest_sub) :
                longest_sub = curr_sub
                break
            else :
                break
        
        
        if idx < len(s) :
            idx += 1
        else :
            break
    
    print(longest_sub)
    return len(longest_sub)



def main () -> None :
    s: str = input("Enter string:  ")
    
    print(f"Length of longest substring is  {len_long_substr(s)}")
    return

if __name__ == "__main__" :
    main()