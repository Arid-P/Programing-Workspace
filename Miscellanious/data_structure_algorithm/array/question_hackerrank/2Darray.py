from icecream import ic 

def hourglassSum(arr):
    hourglassSum = []
    i, j = 0, 0
    
    while i < 4:
        ic(i)
        while j < 4:
            ic(j)
            
            #row 1
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            #row 2
            d = arr[i+1][j+1]
            #row 3
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            ic(a, b,c, d, e, f, g)
            
            hgsum = a + b + c + d + e + f + g
            hourglassSum.append(hgsum)
            ic(hgsum, hourglassSum)
            print()
            j += 1 
        j = 0
        i += 1
    
    return max(hourglassSum)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

