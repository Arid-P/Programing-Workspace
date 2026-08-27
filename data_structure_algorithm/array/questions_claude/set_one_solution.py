from typing import Any, Optional
from icecream import ic
ic.disable()

class Solution:
    def find_second_largest (self, arr: list[int]) -> int:
        max_val= float('-inf')
        answer= float('-inf')
        
        for val in arr:
            if max_val < val:
                answer = max_val
                max_val = val
            elif answer < val:
                answer = val
        
        return answer
    
    def is_palindrome (self, arr: list[Any]) -> bool:
        i, j = 0, -1
        
        while i < len(arr):
            if arr[i] != arr[j]:
                return False
            i += 1 
            j -= 1
        
        return True
    
    def rotate_right(self, arr: list[Any], k: int) -> list[Any]:
        if k > len(arr):
            k = k % len(arr)
        elif k == 0 :
            return arr
        
        i = 0
        iswap = -1 * k
        ic("1. Inistalisation and modulo completed")
        
        if len(arr) % 2 == 0: #length is even
            #decides the number of times the loop should run
            #based upon the len of arr and k
            check = len(arr) - k if (k <= len(arr)/2) else k
            ic("2.e even, check made, outside loop")
            while i < check:
                #swap 
                tmp = arr[i]
                arr[i] = arr[iswap]
                arr[iswap] = tmp
                
                #the condition for iswap values
                iswap += 1 
                if iswap == 0:
                    iswap = -1 * k
                
                i += 1
        else:
            #tells whther k is greater than 
            #half of the length of the array
            #or less than half of the length
            is_greater = True if (k > len(arr)/2) else False
            ic(is_greater)
            while i < len(arr)-1:
                #swap 
                tmp = arr[i]
                arr[i] = arr[iswap]
                arr[iswap] = tmp
                ic(i, arr)
                #the condition for iswap values
                if iswap != -1:
                    iswap += 1
                elif not is_greater:
                    iswap = -1*k
                
                i += 1
                ic(i, iswap)
        
        return arr
    
    def pair_sum (self, arr: list[int], target: int) -> list:
        #the hashmap to lookup the difference (part)
        hashmap: dict[int, bool] = {}
        #the pairs we are looking for
        pairs: list[Optional(tuple(int, int))] = [] 
        
        for num in arr:
            missing_part = target - num 
            
            if hashmap.get(missing_part) :
                pairs.append((missing_part, num))
            
            hashmap[num] = True
        
        return pairs
    
    def two_sum (self, arr: list[int], target: int) -> int:
        #the hashmap to lookup the difference (part)
        hashmap: dict[int, bool] = {}
        
        for idx, num in enumerate(arr):
            ic("second step completed")
            missing_part = target - num 
            ic(num, missing_part, hashmap.get(missing_part))
            
            if hashmap.get(missing_part) is not None:
                return [hashmap.get(missing_part) , idx]
            
            hashmap[num] = idx

ic(Solution().two_sum([2,7,11,15], 9))