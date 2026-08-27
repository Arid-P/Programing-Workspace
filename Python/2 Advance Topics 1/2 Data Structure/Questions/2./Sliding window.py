from collections import deque


def main () -> None :
    #raise ValueError('main not completely implemented')
    arr: list[int] = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3 
    
    right_p, left_p = 0, k
    max_elements: list[int] = []
    
    while left_p <= len(arr) :
        max_elements.append(max ( arr[right_p : left_p] ) )
        right_p += 1 
        left_p += 1
    
    print(max_elements)
    return



"""
Gpt's code


from collections import deque

def main() -> None:
    arr: list[int] = [1, 3, -1, -3, 5, 3, 6, 7]
    k: int = 3
    
    if not arr or k <= 0:
        print([])
        return
    
    max_elements: list[int] = []
    window: deque[int] = deque()  # Stores indices of array elements
    
    for i in range(len(arr)):
        # Remove elements that are outside the current window
        if window and window[0] < i - k + 1:
            window.popleft()
        
        # Remove elements that are smaller than the current element from the back of the deque
        while window and arr[window[-1]] < arr[i]:
            window.pop()
        
        # Add the current element's index to the deque
        window.append(i)
        
        # Add the maximum element of the current window to the result (start adding after the first full window)
        if i >= k - 1:
            max_elements.append(arr[window[0]])
    
    print(max_elements)
    return

if __name__ == "__main__":
    main()
"""