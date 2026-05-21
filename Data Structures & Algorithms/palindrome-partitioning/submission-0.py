class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []
        cache = {}
        def isPalindrome(start, end):
            if start >= end:
                return True
            if (start, end) in cache:
                return cache[(start, end)]
            if s[start] != s[end]:
                return False
            cache[(start, end)] =  isPalindrome(start+1, end-1)
            return cache[(start, end)]
        def backtrack(index):
            if index >= len(s):
                result.append(part.copy())
                return
            for nextIndex in range(index, len(s)):
                if isPalindrome(index, nextIndex):
                    part.append(s[index: nextIndex+1])
                    backtrack(nextIndex+1)
                    part.pop()
        backtrack(0)
        return result