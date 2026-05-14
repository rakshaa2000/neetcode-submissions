class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def dpCalc(index):
            if cache[index] != -1:
                return cache[index]
            lis = 1
            for nextIndex in range(index + 1, n):
                if nums[nextIndex] > nums[index]:
                    lis = max(lis, 1 + dpCalc(nextIndex))
            
            cache[index] = lis
            return lis
        return max(dpCalc(i) for i in range(n))