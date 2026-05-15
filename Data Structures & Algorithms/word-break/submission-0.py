class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictSet = set(wordDict)
        cache = {}
        def dp(index):
            if index == len(s):
                return True
            if index in cache:
                return cache[index]
            for word in dictSet:
                size = len(word)
                if s[index:index+size] == word and dp(index+size):
                    cache[index] = True
                    return True
            cache[index] = False
            return False
        return dp(0)