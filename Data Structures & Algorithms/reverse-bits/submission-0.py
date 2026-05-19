class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        msb = 0
        while n:
            bits[msb] = n % 2
            msb += 1
            n //= 2
        result = 0
        for i in range(31, -1, -1):
            result += bits[31 - i] * 2 ** i
        return result