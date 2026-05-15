class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(index, amount):
            if amount == 0:
                return 0
            if amount < 0 or index == len(coins):
                return 10**5 + 1
            if (index, amount) in cache:
                return cache[(index, amount)]
            include = 1 + dp(index, amount - coins[index])
            exclude = dp(index + 1, amount)
            cache[(index, amount)] = min(include, exclude)
            return cache[(index, amount)]
        minCoins = dp(0, amount)
        return minCoins if minCoins < 10**5 + 1 else -1