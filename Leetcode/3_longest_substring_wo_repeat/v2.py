from itertools import islice

class Solution:
    def lengthOfLongestSubstring(self, s: str, ic) -> int:
        if not s:
            return 0
        
        max_len = 1
        curr_len = 1
        encountered = {s[0] : 0}
        
        i = 1
        extra = 0
        while i < len(s):
            #ic(i, curr_len, max_len)
            #ic(s[i], encountered)
            
            if encountered.get(s[i]) is not None:
                start = encountered.get(s[i]) - extra + 1 if encountered.get(s[0]) == 0 else encountered.get(s[i]) - extra
                extra = encountered.get(s[i])
                #ic(start ,extra, encountered.get(s[i]))
                
                encountered = dict(islice( encountered.items(), start, curr_len))
                curr_len -= start
                #ic(curr_len ,encountered)
                continue
            
            curr_len += 1 
            encountered[s[i]] = i
            
            if curr_len > max_len:
                max_len = curr_len
            
            i += 1

        return max_len if max_len > curr_len else curr_len