import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if not sub or x > sub[-1]:
                sub.append(x)
            else:
                # Find the index of the first element >= x
                idx = bisect.bisect_left(sub, x)
                sub[idx] = x
        return len(sub)