class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        i = len(digits)-1
        while i >= 0:
            sumNow = digits[i] + carry
            carry = sumNow // 10
            digits[i] = sumNow % 10
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits