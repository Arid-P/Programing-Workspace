from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 2e4
        min_price_i = 0
        for idx, price in enumerate(prices):
            if price < min_price:
                min_price = price
                min_price_i = idx
        
        max_price = -1
        for price in prices[min_price_i:]:
            if price > max_price:
                max_price = price
        
        return max_price - min_price