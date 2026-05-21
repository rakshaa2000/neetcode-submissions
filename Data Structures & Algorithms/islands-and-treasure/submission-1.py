class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        INF = 2 ** 31 - 1
        while queue:
            current = queue.popleft()
            for dir in directions:
                row = current[0] + dir[0]
                col = current[1] + dir[1]
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == INF:
                    grid[row][col] = min(grid[row][col], grid[current[0]][current[1]] + 1)
                    queue.append([row, col])