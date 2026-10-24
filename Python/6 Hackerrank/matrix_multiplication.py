import numpy as np


def matrix_print (matrix: list[list[int]]) -> list[list[int]] :
    print("[[ ", end='')
    
    for idx1, row in matrix :
        for idx2, el in enumerate(row, 1) :
            
            if idx2 != len(row) :
                print(f"{el}", end=" ")
            elif idx1 == len(row) and idx1!= len(matrix) :
                print(f"{el}]\n [", end='')
            else :
                print(f"{el}]]")
        
    


def transformation (org_matrix: list[list[any]]) -> list[list[any]] :
    n = len(org_matrix)
    matrix: list[list[any]] = [ ["/"] * n  for _ in range(n)]
    
    for i in range(n) :
        for j in range(n) :
            matrix[i][j] = org_matrix[j][i]
    
    return matrix


def mine_input () -> list[ list[list[int]], list[list[int]], int] :
    n = int(input())
    matrix1: list[list[int]] = []
    matrix2: list[list[int]] = []
    
    for i in range(n) :
        li: list[int] = list( map(int, input().split(" ")) )
        matrix1.append(li)
    
    for i in range(n) :
        li: list[int] = list( map(int, input().split(" ")) )
        matrix2.append(li)
    
    return [matrix1, matrix2, n]


def main () -> None :
    info = mine_input()
    
    arr1: list[list[int]] = np.array(info[0])
    arr2: list[list[int]] = np.array(info[1])
    n: int = info[2]
    
    
    result_matrix: list[list[int]] = [ [0] * n for _ in range(n)]
    arr2 = transformation(arr2)
    
    for i in range(n) :
        row = arr1[i]
        for j in range(n) :
            col = arr2[j]
            product = np.dot(row, col)
            
            result_matrix[i][j] = product
    
    print(result_matrix)
    matrix_print(result_matrix)
    
    return

if __name__ == "__main__" :
    main()
   
"""
2
1 2
3 4
1 2
3 4
"""