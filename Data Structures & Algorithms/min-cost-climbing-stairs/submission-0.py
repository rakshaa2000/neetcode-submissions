class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(index):
            if index >= len(cost):
                return 0
            if index in cache:
                return cache[index]
            oneSkip = cost[index] + dp(index+1)
            twoSkip = cost[index] + dp(index+2)
            cache[index] = min(oneSkip, twoSkip)
            return cache[index]
        return min(dp(0), dp(1))