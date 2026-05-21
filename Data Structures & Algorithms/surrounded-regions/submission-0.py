class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(row, col):
            if 0 <= row < m and 0 <= col < n and board[row][col] == 'O':
                board[row][col] = 'C'
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m-1, j)
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'C':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'