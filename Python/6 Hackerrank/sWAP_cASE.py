def swap_case(s):
    capital_bounds: list = [65, 90]
    smaller_bounds: list = [97, 122]
    
    answer: str = ""
    for chr_ in s :
        #Capital letter case
        if capital_bounds[0] <= ord(chr_) and ord(chr_) <= capital_bounds[1] :
            answer += chr( ord(chr_) + 32 )
        #Small letter case
        elif smaller_bounds[0] <= ord(chr_) and ord(chr_) <= smaller_bounds[1] :
            answer += chr( ord(chr_) - 32 )
        #Id any other chr other than alphabet
        else :
            answer += chr_
    
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)