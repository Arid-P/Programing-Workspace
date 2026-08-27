from v3 import Solution as sol
from icecream import ic 

def main () -> None:
    s = sol()
    test_cases = [
        [7,1,5,3,6,4],
        [7,6,4,3,1],
        [2,4,1], #v2
        [7,2,4,1]
    ]
    
    for t in test_cases:
        ic(t)
        result = s.maxProfit(t, ic)
        ic(result)
        ic("-"*25)
    
if __name__ == "__main__" :
    main()