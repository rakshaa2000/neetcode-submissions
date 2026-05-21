class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        result = []
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
            index += 1
        result.append(newInterval)
        while index < len(intervals):
            result.append(intervals[index])
            index += 1
        return result