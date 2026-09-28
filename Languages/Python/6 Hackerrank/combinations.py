# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement


def main () -> None :
    s, k = input().split(" ")
    org_k = int(k)
    
    org_per: list[any] = []
    for k in range(1, org_k+1, 1) :
        org_per.append(list(combinations_with_replacement(s, k)))
    
    
    per = []
    for op in org_per :
        op = list( map( lambda el: sorted(el) , op) )
        op = list( map( lambda el: ''.join(el), op) )
        
        op = sorted(op)
        for el in op :
            per.append(el)
    
    for p in per :
        print(p)
    
    return 

if __name__ == '__main__' :
    main()
