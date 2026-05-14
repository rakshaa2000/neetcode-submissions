class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(index, buy):
            if index >= len(prices):
                return 0
            if (index, buy) in cache:
                return cache[(index, buy)]
            if buy:
                profitNow = -prices[index] + dp(index+1, not buy)
                profitLater = dp(index+1, buy)
                cache[(index, buy)] =  max(profitNow, profitLater)
            else:
                profitNow = prices[index] + dp(index+2, not buy)
                profitLater = dp(index+1, buy)
                cache[(index, buy)] = max(profitNow, profitLater)
            return cache[(index, buy)]
        return dp(0, True)
