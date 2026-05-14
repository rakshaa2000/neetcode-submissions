class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(index, amount):
            if amount == 0:
                return 1
            if amount < 0 or index == len(coins):
                return 0
            if (index, amount) in cache:
                return cache[(index, amount)] 
            include = dp(index, amount - coins[index])
            exclude = dp(index+1, amount)
            cache[(index, amount)] = include + exclude
            return cache[(index, amount)] 
        return dp(0, amount)