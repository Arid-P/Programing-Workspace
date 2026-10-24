import numpy

def mine_input () -> list[list[int]] :
    n, m = list( map(int, input().split(" ")) )
    matrix: list[list[int]] = []
    
    for i in range(n) :
        li: list[int] = list( map(int, input().split(" ")) )
        matrix.append(li)
    
    return matrix


def main () -> None :
    matrix: list[list[int]] = mine_input()
    matrix = numpy.array(matrix)
    
    matrix = numpy.sum(matrix, axis=0)
    #print(matrix)
    matrix = numpy.prod(matrix)
    print(matrix)
    
    
    return

if __name__ == "__main__" :
    main()