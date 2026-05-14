class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.perms = []
        self.permutations(0, nums)
        return self.perms

    def permutations(self, index, nums):
        if index == len(nums):
            self.perms.append(nums[:])
            return
        for nextIndex in range(index, len(nums)):
            nums[index], nums[nextIndex] = nums[nextIndex], nums[index]
            self.permutations(index + 1, nums)
            nums[index], nums[nextIndex] = nums[nextIndex], nums[index]