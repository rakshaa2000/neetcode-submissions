class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dpCalc(index, target):
            if target == 0 and index == len(nums):
                return 1
            if index == len(nums):
                return 0
            if (index, target) in cache:
                return cache[(index, target)]
            positive = dpCalc(index+1, target - nums[index])
            negative = dpCalc(index+1, target + nums[index])
            cache[(index, target)] = positive + negative
            return cache[(index, target)]
        return dpCalc(0, target)
