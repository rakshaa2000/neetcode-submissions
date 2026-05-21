class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        board = [['.'] * n for _ in range(n)]
        def backtrack(board, row):
            def possible(row, col):
                for i in range(n):
                    if board[i][col] == 'Q':
                        return False
                i, j = row - 1, col - 1
                while i >= 0 and j >= 0:
                    if board[i][j] == 'Q':
                        return False
                    i -= 1
                    j -= 1
                i, j = row - 1, col + 1
                while i >= 0 and j < n:
                    if board[i][j] == 'Q':
                        return False
                    i -= 1
                    j += 1
                return True
            if row == n:
                boards.append(["".join(r) for r in board])
                return
            for col in range(n):
                if possible(row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        backtrack(board, 0)
        return boards