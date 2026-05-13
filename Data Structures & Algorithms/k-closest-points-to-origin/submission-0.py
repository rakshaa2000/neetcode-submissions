class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[-1 * (points[i][0] ** 2 + points[i][1] ** 2), i] for i in range(len(points))]
        heap = []
        heapq.heapify(heap)
        for element in distances:
            heapq.heappush(heap, element)
            if len(heap) > k:
                smallest = heapq.heappop(heap)
        results = []
        while len(heap) > 0:
            top = heapq.heappop(heap)
            results.append(points[top[1]])
        return results