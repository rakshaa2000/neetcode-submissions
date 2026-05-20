class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        results = [intervals[0]]
        for start, end in intervals:
            lastEnd = results[-1][1]
            if start <= lastEnd:
                results[-1][1] = max(lastEnd, end)
            else:
                results.append([start, end])
        return results