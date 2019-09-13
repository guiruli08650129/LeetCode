class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        minPrice = sys.maxsize
        profit = 0
        for p in prices:
            if minPrice >= p:
                minPrice = p
            else:
                if p - minPrice > profit:
                    profit = p - minPrice
        
        return profit