class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dp(i, j):
            if j == len(t):
                return 1
            if i >= len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            exclude = dp(i+1, j)
            if s[i] == t[j]:
                include = dp(i+1, j+1)
                cache[(i, j)] = include + exclude
            else:
                cache[(i, j)] = exclude
            return cache[(i, j)]
        return dp(0, 0)