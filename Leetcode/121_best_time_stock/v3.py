from typing import List, Tuple, Optional

class Solution:
    def get_min_idx (self, nums: List[int]) -> Tuple[int]:
        min_ = 2e4
        min_idx = 0
        for idx, num in enumerate(nums):
            if num < min_:
                min_ = num
                min_idx = idx
        
        return min_, min_idx
    
    def get_max_idx (self, nums: List[int]) -> Tuple[int]:
        max_ = -1
        max_idx = 0
        for idx, num in enumerate(nums):
            if num > max_:
                max_ = num
                max_idx = idx
        
        return max_, max_idx
    
    def linearProfit (self, prices: List[int]) -> int :
        min_price, min_price_idx = self.get_min_idx(prices)
        max_price, _ = self.get_max_idx(prices[min_price_idx:])
        
        return max_price - min_price
    
    def reverseProfit (self, prices: List[int]) -> int:
        max_price, max_price_idx = self.get_max_idx(prices)
        min_price, _ = self.get_min_idx(prices[:max_price_idx])
        
        return max_price - min_price
    
    def adjacentdiff (self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        
        i = 1
        diff = nums[1] - nums[0]
        
        while i < len(nums):
            if nums[i] - nums[i-1] > diff :
                diff = nums[i] - nums[i-1]
            i += 1
        
        return diff
    
    def maxProfit(self, prices: List[int], ic) -> int:
        i = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                break
            i += 1
        else:
            return 0
        
        result1 = self.linearProfit(prices)
        result2 = self.reverseProfit(prices)
        result3 = self.adjacentdiff(prices)
        ic(print, result1, result2, result3)
        return max(result1, result2, result3)