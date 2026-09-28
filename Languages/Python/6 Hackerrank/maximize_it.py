
def main () -> None :
    #input 
    no_list, M = list( map(int, input().split(" ")) )
    
    lists: list[list[int]] = []
    for i in range(no_list) :
        list_ = list( map(int, input().split(" ")) )[1 : ]
        list_.sort(reverse=True)
        lists.append(list_)
    
    #processing
    total_sum: int = 0
    for list_ in lists :
        max_el: int = list_[0]%M
        total_sum += max_el**2
    
    answer: int = total_sum % M
    #output
    print(answer)
    
    return

if __name__ == "__main__" :
    main()

