class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def path(x, y):
            if x == m-1 and y == n-1:
                return 1
            if x == m or y == n:
                return 0
            if (x, y) in cache:
                return cache[(x, y)]
            down = path(x, y+1)
            right = path(x+1, y)
            paths = down + right
            cache[(x, y)] = paths
            return paths
        return path(0, 0)