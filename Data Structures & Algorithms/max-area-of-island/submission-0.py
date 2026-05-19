class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def maxArea(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            area = 1
            grid[x][y] = 0
            for direct in directions:
                area += maxArea(x + direct[0], y + direct[1])
            return area

        result = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]:
                    result = max(maxArea(i, j), result)

        return result