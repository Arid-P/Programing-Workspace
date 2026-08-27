from icecream import ic 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_len = 1
        curr_len = 1
        encountered = [s[0]]
        
        for i in range(1, len(s)):
            if s[i] not in encountered:
                curr_len += 1 
                encountered.append(s[i])
            else:
                if curr_len > max_len:
                    max_len = curr_len
                encountered = [s[i]]
                curr_len = 1
        
        return max_len if max_len > curr_len else curr_len