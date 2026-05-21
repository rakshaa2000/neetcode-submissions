class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJump = 0
        curJump = 0
        jumps = 0
        for i in range(len(nums)-1):
            maxJump = max(maxJump, i + nums[i])
            if curJump == i:
                curJump = maxJump
                jumps += 1
        return jumps