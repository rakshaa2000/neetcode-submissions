class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]:
                return False
            board[x][y] = '#'
            found = False
            for direction in directions:
                found = found or dfs(x + direction[0], y + direction[1], index + 1)
            board[x][y] = word[index]
            return True if found else False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    found = dfs(i, j, 0)
                    if found:
                        return True
        return False