from itertools import islice

class Solution:
    def lengthOfLongestSubstring(self, s: str, ic) -> int:
        if not s:
            return 0
        
        max_len = 1
        curr_len = 1
        encountered = {s[0] : 0}
        
        i = 1
        old = 0
        left, right = 0, 1
        while right < len(s):
            ic("start")
            ic(left, right, curr_len, max_len)
            ic(s[right], encountered)
            
            if encountered.get(s[right]) is not None and left <= encountered.get(s[right]) <= right:
                diff = encountered.get(s[right]) - old + 1 if left == 0 else encountered.get(s[right]) - old
                old = encountered.get(s[right]) 
                
                left = encountered.get(s[right]) + 1
                curr_len -= diff
                
                ic(left, diff, old)
                ic(curr_len, encountered)
            
            curr_len += 1 
            encountered[s[right]] = i
            
            if curr_len > max_len:
                max_len = curr_len
            
            right += 1
            ic("end", right, curr_len, encountered)

        return max_len if max_len > curr_len else curr_len