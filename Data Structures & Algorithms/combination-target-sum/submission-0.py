class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current = []
        def combination(nums, index, target, results, current):
            if index == len(nums) or target < 0:
                return
            if target == 0:
                results.append(current.copy())
                return
            current.append(nums[index])
            combination(nums, index, target - nums[index], results, current)
            current.pop()
            combination(nums, index+1, target, results, current)
            return

        combination(nums, 0, target, results, current)
        return results