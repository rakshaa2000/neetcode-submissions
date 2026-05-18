class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dp(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            maxCoins = 0
            for i in range(left, right + 1):
                coins = nums[left-1] * nums[i] * nums[right+1]
                coins += dp(left, i-1) + dp(i+1, right)
                maxCoins = max(maxCoins, coins)
            cache[(left, right)] = maxCoins
            return maxCoins
        return dp(1, len(nums)-2)