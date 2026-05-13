from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        good = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good += 1
                if grid[i][j] == 2:
                    queue.append([i, j])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        time = 0
        while len(queue) > 0 and good > 0:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                for direction in directions:
                    x = direction[0] + front[0]
                    y = direction[1] + front[1]
                    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        good -= 1
                        queue.append([x, y])
            time += 1
        return time if good == 0 else -1