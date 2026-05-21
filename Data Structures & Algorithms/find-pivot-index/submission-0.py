class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result = [0]
        for num in nums:
            result.append(result[-1] + num)
        total = result[-1]
        for i in range(1, len(result)):
            if total - result[i] == result[i-1]:
                return i-1
        return -1