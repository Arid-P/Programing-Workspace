#1222311
def main () -> None :
    s = input()
    
    answer: str = "" 
    
    while s :
        curr_el = s[0]
        count = 1
        
        for el in s[1 :] :
            if el == curr_el :
                count += 1
            else :
                break
            
        s = s[count : ]
        
        if s :
            answer += f'({count}, {curr_el}), '
        else :
            answer += f'({count}, {curr_el})'
        
        
    
    print(answer)
    
    return

if __name__ == "__main__" :
    main()