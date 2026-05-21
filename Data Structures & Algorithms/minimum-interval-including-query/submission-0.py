class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        result = {}
        index = 0
        for query in sorted(queries):
            while index < len(intervals) and intervals[index][0] <= query:
                start, end = intervals[index]
                heapq.heappush(minHeap, (end - start + 1, end))
                index += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            result[query] = minHeap[0][0] if minHeap else -1
        return [result[q] for q in queries]