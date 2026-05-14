class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dp(index):
            if index == len(s):
                return 1
            if index > len(s) or s[index] == '0':
                return 0
            if index in cache:
                return cache[index]
            singleDigit = 0
            doubleDigit = 0
            singleDigit = dp(index+1)
            if int(s[index:index+2]) <= 26:
                doubleDigit = dp(index+2)
            cache[index] = singleDigit + doubleDigit
            return cache[index]
        return dp(0)