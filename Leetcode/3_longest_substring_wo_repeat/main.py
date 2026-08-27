from v3 import Solution as sol
from icecream import ic 

def main () -> None:
    s = sol()
    test_cases = [
        "pwwekw",
        "abcabcbb",
        "bbbb",
        "dvdf",
        "abcdecfghe",
        "",
        "bbtablud"
    ]
    
    for t in test_cases:
        ic(t)
        result = s.lengthOfLongestSubstring(t, ic)
        ic.enable()
        ic(result)
        print()
        ic("-"*25)
    
if __name__ == "__main__" :
    main()