class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = {}
        def isPalindrome(i, j):
            if i >= j:
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] != s[j]:
                cache[(i, j)] = False
                return False
            cache[(i, j)] = isPalindrome(i+1, j-1)
            return cache[(i, j)]
        maxLen = float('-inf')
        start = -1
        end = -1
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if isPalindrome(i, j) and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i
                    end = j
        return s[start:end+1]