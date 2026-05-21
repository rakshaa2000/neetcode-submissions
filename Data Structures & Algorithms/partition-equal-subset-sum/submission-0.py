class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        fullTotal = sum(nums)
        if fullTotal % 2:
            return False
        halfTotal = fullTotal // 2
        def dp(index, total):
            if total == 0:
                return True
            if total < 0 or index == len(nums):
                return False
            if (index, total) in cache:
                return cache[(index, total)]
            include = dp(index+1, total - nums[index])
            exclude = dp(index+1, total)
            cache[(index, total)] = include or exclude
            return cache[(index, total)]
        return dp(0, halfTotal)
