class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        pacificQ = deque()
        atlanticQ = deque()
        for i in range(n):
            pacificQ.append((0, i))
            atlanticQ.append((m - 1, i))
        for i in range(m):
            pacificQ.append((i, 0))
            atlanticQ.append((i, n - 1))

        def valid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def bfs(queue, visited):
            while queue:
                size = len(queue)
                for i in range(size):
                    row, col = queue.popleft()
                    visited[row][col] = True
                    for direct in directions:
                        newRow = row + direct[0]
                        newCol = col + direct[1]
                        if (
                            valid(newRow, newCol)
                            and not visited[newRow][newCol]
                            and heights[row][col] <= heights[newRow][newCol]
                        ):
                            queue.append((newRow, newCol))
            return visited
        
        pacific = bfs(pacificQ, pacific)
        atlantic = bfs(atlanticQ, atlantic)
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result