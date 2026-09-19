from icecream import ic

""" brute force:
    arr = [0] * n
    
    for query in queries:
        a, b, k = query
        
        for i in range(a-1, b):
            arr[i] += k 
    
    return max(arr)
"""
"""Greedy Method 
    answer_idx = queries[0][:2]
    answer = queries[0][2]
    ic(answer, answer_idx)
    
    for i in range(1, len(queries)):
        a, b, k = queries[i]
        ic(a, b, k)
        
        if answer_idx[0] <= b and answer_idx[1] >= a:
            answer += k
            answer_idx[0] = a if answer_idx[0] < a else answer_idx[0]
            answer_idx[1] = a if answer_idx[1] > b else answer_idx[0]
        elif answer < k:
            answer = k
            answer_idx = [a, b]
        ic(answer, answer_idx)
    
    return answer 
    """
def arrayManipulation(n, queries):
    #The Difference Array Method
    arr = [0] * n 
    
    for q in queries:
        a, b, k = q 
        
        arr[a-1] += k 
        if b < n:
            arr[b] -= k
    #ic(arr)
    
    max_value = arr[0]
    for i in range(1, n):
        arr[i] = arr[i-1] + arr[i]
        if arr[i] > max_value:
            max_value = arr[i]
        i += 1
        #ic(arr)
    
    return max_value
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    ic(result)
