class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dp(i, j):
            if i == len(word1) or j == len(word2):
                return max(len(word1) - i, len(word2) - j)
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i, j)] =  dp(i+1, j+1)
            else:
                cache[(i, j)] = 1 + min(dp(i+1, j), dp(i+1, j+1), dp(i, j+1))
            return cache[(i, j)]

        return dp(0, 0)