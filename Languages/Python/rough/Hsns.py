from itertools import repeat

def main () -> None :
    num = 0
    
    for i in repeat(1, 93) :
        num = num * 10 + i
    
    num = num * (10 ** 7)
    num = num + 4299125
    
    num = str(num)
    print(num[0 : 71])
    print(num[71 : ])
    
    # num2 = 0
#     k = 70
#     for i in repeat(1, 5) :
#         for i in repeat(1, k) :
#             num2 = num2 * 10 + i
#         print(k)
#         print(num2)
#         k += 1
#         num2 = 0
    
    print(len(num))
    
    return

if __name__ == "__main__" :
    main()