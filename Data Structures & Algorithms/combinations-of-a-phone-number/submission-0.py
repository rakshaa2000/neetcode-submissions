class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {'2' : "abc", '3' : "def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        result = []
        def backtrack(index, current):
            if index == len(digits) and current:
                result.append(current)
                return None
            if index == len(digits):
                return None
            for ch in letter[digits[index]]:
                current += ch
                backtrack(index+1, current)
                current = current[:-1]
        backtrack(0, "")
        return result