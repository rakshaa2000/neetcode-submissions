class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        expectedTotal = int(len(nums) * (len(nums) + 1)/2)
        return expectedTotal - total