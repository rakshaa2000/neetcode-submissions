class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dp(index):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]
            include = nums[index] + dp(index+2)
            exclude = dp(index+1)
            cache[index] = max(include, exclude)
            return cache[index]
        return max(dp(0), dp(1))
