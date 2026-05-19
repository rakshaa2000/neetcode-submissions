class UnionFind:
    def __init__(self, n):
        self.parent = {i : i for i in range(1, n+1)}
        self.connected = n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        self.connected -= 1
        self.parent[rootY] = rootX
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            connect = uf.union(edge[0], edge[1])
            if not connect:
                return edge
        return [-1, -1]