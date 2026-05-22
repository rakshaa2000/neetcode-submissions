class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)]
        visited = set()
        time = 0
        while minHeap:
            weight, current = heapq.heappop(minHeap)
            if current in visited:
                continue
            visited.add(current)
            time = weight

            for neighbour, edgeWeight in edges[current]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (edgeWeight + weight, neighbour))
        return time if len(visited) == n else -1