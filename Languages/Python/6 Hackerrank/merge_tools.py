#AABCAAADA

from itertools import repeat 

def merge_the_tools(string, k) -> None:
    s_ptr, e_ptr = 0, k 
    
    while e_ptr <= len(string) :
        sub_str = string[s_ptr : e_ptr]
        answer = ""
        
        for i in repeat(0, k) :
            chr_ = sub_str[i]
            answer += chr_
            
            sub_str = sub_str.replace(chr_, "")
            if not sub_str :
                break
        
        s_ptr += k
        e_ptr += k
        
        print(answer)
    
    return 


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)