class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
    def countBits(self, n: int) -> List[int]:
        setBits = [self.hammingWeight(i) for i in range(0, n+1)]
        return setBits