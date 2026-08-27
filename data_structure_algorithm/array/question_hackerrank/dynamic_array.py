from icecream import ic 

def dynamicArray(n, queries):
    #initialising the variables
    arr = [[] for i in range(n)]
    lastanswer = 0
    answers = []
    
    ic(arr)
    for query in queries:
        type_query, x, y = query
        idx = x ^ lastanswer
        idx = idx % n 
        ic(idx)
        
        if type_query == 1:
            arr[idx].append(y)
        else:
            lastanswer = arr[idx][y % len( arr[idx] )]
            answers.append(lastanswer)
    
    return answers


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    ic(result)
