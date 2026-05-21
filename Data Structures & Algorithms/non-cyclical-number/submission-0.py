class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(num):
            total = 0
            while num:
                total += (num % 10) ** 2
                num //= 10
            return total
        
        fast, slow = sq(n), n

        while fast != 1:
            fast = sq(sq(fast))
            slow = sq(slow)
            if fast == slow:
                return False
        return True