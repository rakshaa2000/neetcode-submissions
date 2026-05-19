class UnionFind:
    def __init__(self, n):
        self.parent = {i : i for i in range(n)}
        self.connected = n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return False
        self.parent[rooty] = rootx
        self.connected -= 1
        return True
    def isConnected(self):
        return self.connected 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.isConnected()