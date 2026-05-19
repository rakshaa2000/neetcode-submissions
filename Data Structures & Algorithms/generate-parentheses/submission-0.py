class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(opened, closed, current):
            if opened == n and closed == n:
                result.append(current)
                return
            if closed > opened:
                return
            if opened < n:
                backtrack(opened+1, closed, current + '(')
            if closed < n:
                backtrack(opened, closed+1, current + ')')
        backtrack(0, 0, "")
        return result