class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        current = []
        def combination(candidates, target, index):
            if target == 0:
                results.append(current.copy())
                return
            if target < 0 or index == len(candidates):
                return
            current.append(candidates[index])
            combination(candidates, target - candidates[index], index + 1)
            current.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            combination(candidates, target, index+1)
        combination(candidates, target, 0)
        return results