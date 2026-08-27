def main () -> None :
    no_shoes: int = int(input())
    shoe_sizes: list[int] = list( map(int, input().split(" ")))
    
    no_customers: int = int(input())
    customers_wants: list[list[int, int]] = []
    for i in range(no_customers) :
        want_info = list(map(int, input().split(" ")))
        customers_wants.append(want_info)
    
    money_recived: list[int] = []
    for want_info in customers_wants :
        shoe_size = want_info[0]
        price = want_info[1]
        
        if shoe_size in shoe_sizes :
            money_recived.append(price)
            shoe_sizes.remove(shoe_size)
    
    print(sum(money_recived))
    
    return

if __name__ == "__main__" :
    main()