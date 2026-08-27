from collections import deque


def main () -> None :
    arr: list = [2, 1, 5, 1, 3, 2]
    k: int = 3
    
    subarr = deque(arr[:k]) #silicing the arr 
    max_sum: float = sum(list(subarr)) # sum of the first sub arr
    current_sum: float = max_sum
    max_subarr: list = list(subarr)

    for val in arr[k:] :
        #finding its some
        current_sum = current_sum - subarr[0] + val
        
        #updating the deque
        subarr.popleft()
        subarr.append(val)
    
        if max_sum < current_sum :
            max_sum = current_sum
            max_subarr = list(subarr)

    print(max_subarr)
    return 

if __name__ == "__main__" :
    main()