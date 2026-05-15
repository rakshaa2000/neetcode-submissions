class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        cache2 = {}
        if len(nums) == 1: return nums[0]
        nums1, nums2 = nums[:-1], nums[1:]
        def dp(index, nums, cache):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]
            include = nums[index] + dp(index+2, nums, cache)
            exclude = dp(index+1, nums, cache)
            cache[index] = max(include, exclude)
            return cache[index]
        return max(dp(0, nums1, cache), dp(0, nums2, cache2))
