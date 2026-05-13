class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        remaining = []
        heapq.heapify(remaining)
        for stone in stones:
            heapq.heappush(remaining, -stone)
        while len(remaining) > 0:
            stone1 = -heapq.heappop(remaining)
            if len(remaining) == 0:
                return stone1
            stone2 = -heapq.heappop(remaining)
            if stone1 - stone2 > 0:
                heapq.heappush(remaining, stone2 - stone1)
        return 0