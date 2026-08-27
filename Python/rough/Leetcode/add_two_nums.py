
def sum (li: list[str]) -> str :
    string: str = ""
    for chr_ in li :
        string += chr_
    
    return string


def add_list_nums (l1, l2) -> None :
    #To reverse rhe list
    l1.reverse()
    l2.reverse()
    n1: int = int(sum(l1))
    n2: int = int(sum(l2))
    
    print(f"{n1=},   {n2=}")
    
    total: str = [int(chr_) for chr_ in str(n1 + n2)]
    total.reverse()
    return total


def main () -> None :
    l1: list[int] = list( input("Enter the list 1 :  ").strip().split(',') )
    
    l2: list[int] = list( input("Enter the list 2 :  ").strip().split(',') )
    
    #l1 = ['2', '4', '3']
    #l2 = ['5', '6', '4']
    print(f"\nlist: {add_list_nums(l1, l2)}")
    
    #print(f"The index are: {two_num_sum_target(nums, target)}")
    
    return

if __name__ == "__main__" :
    main()