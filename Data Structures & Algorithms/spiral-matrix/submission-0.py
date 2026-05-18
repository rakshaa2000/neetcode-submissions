class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direction = 1
        elements = []
        row, col = 0, -1
        while m and n:
            for i in range(n):
                col += direction
                elements.append(matrix[row][col])
            m -= 1
            for i in range(m):
                row += direction
                elements.append(matrix[row][col])
            n
            n -= 1
            direction *= -1
        return elements