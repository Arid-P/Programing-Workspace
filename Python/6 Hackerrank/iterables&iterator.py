from itertools import combinations 


def main () -> None :
    n = int(input())
    
    chrs = input().split(" ")
    
    k = int(input())
    
    idx_a = [i+1 for i, chr_ in enumerate(chrs) if chr_ == "a"]
    idx_list = list(range(1, n+1))
    
    all_idx_poss = list( map (lambda tup: tuple( map(int, tup)), list( combinations(idx_list, k) )) )
    
    total_outcomes = len(all_idx_poss)
    
    count = 0
    
    for idx in idx_a :
        encountered = []
        
        for el in all_idx_poss :
            if idx in el :
                count += 1
                encountered.append(el)
        
        all_idx_poss = list(set(all_idx_poss) - set(encountered))
        
    
    probability = count/total_outcomes
    
    print(f"{probability:.5f}")
    
    
    return

if __name__ == "__main__" :
    main()