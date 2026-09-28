def check(num: int, count: list[int]) -> list[int, int, int] :
    if num % 3 == 0 :
        count[0] += 1
    if num % 5 == 0 :
        count[1] += 1
    if num % 7 == 0 :
        count[2] += 1
    
    return count


def main () -> None :
    
    for i in range(1, 7, 1) :
        count3 = 0
        count5 = 0
        count7 = 0
        
        count = [count3, count5, count7]
        
        for num in range(1, 15*i + 1, 1) :
            count = check(num, count)
        
        print(f"{15 * i = }")
        print(f"{count[0] = }")
        print(f"{count[1] = }")
        print(f"{count[2] = }")
        print()
        print()
    
    
    return

if __name__ == "__main__" :
    main()